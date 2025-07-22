import cv2

def draw_detections(image, detections):
    for obj in detections:
        left, top, right, bottom = obj.box
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        label = f"{obj.name}: {obj.confidence:.2f}"
        cv2.putText(image, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image
