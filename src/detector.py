import cv2
import numpy as np

class DetectedObject:
    def __init__(self, name, confidence, box):
        self.name = name
        self.confidence = confidence
        self.box = box

class ObjectDetector:
    def __init__(self, model_path, config_path, labels_path, conf_threshold=0.5):
        self.net = cv2.dnn.readNetFromTensorflow(model_path, config_path)
        with open(labels_path, 'r') as f:
            self.labels = [line.strip() for line in f.readlines()]
        self.conf_threshold = conf_threshold

    def detect(self, image):
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True, crop=False)
        self.net.setInput(blob)
        detections = self.net.forward()
        results = []
        for detection in detections[0, 0, :, :]:
            confidence = float(detection[2])
            if confidence > self.conf_threshold:
                class_id = int(detection[1])
                label = self.labels[class_id - 1] if class_id <= len(self.labels) else 'unknown'
                box = detection[3:7] * np.array([w, h, w, h])
                (left, top, right, bottom) = box.astype("int")
                results.append(DetectedObject(label, confidence, (left, top, right, bottom)))
        return results
