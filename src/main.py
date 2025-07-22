import cv2
import sys
from detector import ObjectDetector
from image_utils import draw_detections

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Object Detection App")
    parser.add_argument("--image", required=True, help="Path to input image")
    parser.add_argument("--model", default="../models/frozen_inference_graph.pb", help="Path to model")
    parser.add_argument("--config", default="../models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt", help="Path to config")
    parser.add_argument("--labels", default="../coco.names", help="Path to labels file")
    parser.add_argument("--output", default="output.jpg", help="Path to save output image")
    args = parser.parse_args()

    detector = ObjectDetector(args.model, args.config, args.labels)
    image = cv2.imread(args.image)
    if image is None:
        print("Error: Unable to read image file.")
        sys.exit(1)
    detections = detector.detect(image)

    # Wypisywanie wykrytych obiektów w terminalu
    if detections:
        print("Detected objects:")
        for obj in detections:
            name = obj.name
            confidence = obj.confidence
            box = obj.box
            print(f"Object: {name}, Confidence: {confidence:.2f}, Position: {box}")
    else:
        print("No objects detected.")

    image = draw_detections(image, detections)
    cv2.imwrite(args.output, image)
    print(f"Detected {len(detections)} objects. Result saved to {args.output}")

if __name__ == "__main__":
    main()
