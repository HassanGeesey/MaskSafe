import cv2
import numpy as np
import time

def main():
    # Paths
    weights_path = 'yolov3_mask_last.weights'
    cfg_path = 'detect_mask.cfg'
    names_path = 'mask.names'

    # Load class names
    with open(names_path, 'r') as f:
        classes = [line.strip() for line in f.readlines()]
    
    # Colors for each class: Mask (Green), Improperly (Orange), No Mask (Red)
    # BGR format
    colors = {
        0: (0, 255, 0),    # mask
        1: (0, 165, 255),  # improperly (Orange)
        2: (0, 0, 255)     # no mask
    }

    # Load YOLO
    print("Loading YOLO model...")
    net = cv2.dnn.readNet(weights_path, cfg_path)
    
    # Use CPU by default for stability
    # If you have GPU setup with OpenCV, you can uncomment the CUDA lines
    # net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    # net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    print("Backend: CPU")

    layer_names = net.getLayerNames()
    try:
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    except:
         output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Open Webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Starting video stream. Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        height, width, channels = frame.shape

        # Detecting objects
        # 1/255 = 0.00392
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                
                # Filter out weak predictions
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Non-max suppression
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                class_id = class_ids[i]
                label = str(classes[class_id])
                confidence = confidences[i]
                
                color = colors.get(class_id, (255, 255, 255))
                
                # Draw box
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                
                # Draw label
                text = f"{label} {confidence:.2f}"
                cv2.rectangle(frame, (x, y - 20), (x + w, y), color, -1) # Background for text
                cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        cv2.imshow("Face Mask Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
