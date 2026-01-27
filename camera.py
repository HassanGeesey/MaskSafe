import cv2
import numpy as np

class VideoCamera:
    def __init__(self, weights_path='yolov3_mask_last.weights', cfg_path='detect_mask.cfg', names_path='mask.names'):
        self.weights_path = weights_path
        self.cfg_path = cfg_path
        self.names_path = names_path
        
        # Load class names
        with open(self.names_path, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]

        # Colors: Mask (Green), Improperly (Orange), No Mask (Red)
        self.colors = {
            0: (0, 255, 0),    # mask
            1: (0, 165, 255),  # improperly
            2: (0, 0, 255)     # no mask
        }

        # Initialize YOLO
        print("Loading YOLO model...")
        self.net = cv2.dnn.readNet(self.weights_path, self.cfg_path)
        
        # Backend settings (CPU by default for stability)
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

        self.layer_names = self.net.getLayerNames()
        try:
            self.output_layers = [self.layer_names[i - 1] for i in self.net.getUnconnectedOutLayers()]
        except:
             self.output_layers = [self.layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

    def get_frame(self, frame):
        # This function takes a raw frame, processes it, and returns the processed frame
        height, width, channels = frame.shape

        # Detection
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
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
                
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                class_id = class_ids[i]
                label = str(self.classes[class_id])
                confidence = confidences[i]
                color = self.colors.get(class_id, (255, 255, 255))
                
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                text = f"{label} {confidence:.2f}"
                cv2.rectangle(frame, (x, y - 20), (x + w, y), color, -1)
                cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        
        return frame
