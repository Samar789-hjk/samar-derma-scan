import unittest
import numpy as np

from src.predict import predict_image


class PredictImageTests(unittest.TestCase):
    def test_predict_image_returns_valid_output(self):
        image = np.zeros((64, 64, 3), dtype=np.uint8)
        disease, confidence = predict_image(image)

        self.assertIsInstance(disease, str)
        self.assertTrue(disease)
        self.assertIsInstance(confidence, float)
        self.assertGreaterEqual(confidence, 0.0)
        self.assertLessEqual(confidence, 100.0)


if __name__ == "__main__":
    unittest.main()
