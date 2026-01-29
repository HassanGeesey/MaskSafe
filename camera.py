import cv2
import numpy as np
import threading
import time

class VideoStream:
    """Helper class to capture frames in a separate thread for zero latency."""
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src, cv2.CAP_DSHOW)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.stream.set(cv2.CAP_PROP_FPS, 30)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        threading.Thread(target=self.update, args=(), daemon=True).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                self.stream.release()
                return
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True

class VideoCamera:
    def __init__(self, weights_path='yolov3_mask_last.weights', cfg_path='detect_mask.cfg', names_path='mask.names'):
        self.weights_path = weights_path
        self.cfg_path = cfg_path
        self.names_path = names_path
        
        with open(self.names_path, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]

        self.colors = {
            0: (0, 255, 0),    # mask
            1: (0, 165, 255),  # improperly
            2: (0, 0, 255)     # no mask
        }

        print("Loading YOLO model on CPU...")
        self.net = cv2.dnn.readNet(self.weights_path, self.cfg_path)
        
        # Optimization for CPU
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

        self.layer_names = self.net.getLayerNames()
        try:
            self.output_layers = [self.layer_names[i - 1] for i in self.net.getUnconnectedOutLayers()]
        except:
             self.output_layers = [self.layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

        # Performance Variables
        self.frame_count = 0
        self.skip_frames = 3  # Process every 4th frame
        self.last_results = []

    def get_frame(self, frame):
        if frame is None:
            return None
            
        height, width, _ = frame.shape

        # Detection logic
        if self.frame_count % (self.skip_frames + 1) == 0:
            # 320x320 is a good bridge for CPU quality and speed
            blob = cv2.dnn.blobFromImage(frame, 1/255.0, (320, 320), (0, 0, 0), True, crop=False)
            self.net.setInput(blob)
            outs = self.net.forward(self.output_layers)

            class_ids = []
            confidences = []
            boxes = []

            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    
                    if confidence > 0.4: # Slightly lower threshold for CPU speed
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)

                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.3)
            
            self.last_results = []
            for i in range(len(boxes)):
                if i in indexes:
                    self.last_results.append({
                        'box': boxes[i],
                        'class_id': class_ids[i],
                        'confidence': confidences[i]
                    })

        self.frame_count += 1

        for res in self.last_results:
            x, y, w, h = res['box']
            class_id = res['class_id']
            label = self.classes[class_id]
            confidence = res['confidence']
            color = self.colors.get(class_id, (255, 255, 255))
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        return frame
