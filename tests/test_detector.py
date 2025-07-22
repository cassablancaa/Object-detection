import unittest
import cv2
from src.detector import ObjectDetector

class TestObjectDetector(unittest.TestCase):
    def setUp(self):
        self.detector = ObjectDetector(
            model_path="models/frozen_inference_graph.pb",
            config_path="models/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt",
            labels_path="coco.names"
        )
        self.image = cv2.imread("tests/test_image.jpg")  # Dodaj przykładowy obraz testowy

    def test_detection(self):
        detections = self.detector.detect(self.image)
        self.assertIsInstance(detections, list)
        self.assertTrue(all(hasattr(obj, 'name') for obj in detections))

if __name__ == '__main__':
    unittest.main()
