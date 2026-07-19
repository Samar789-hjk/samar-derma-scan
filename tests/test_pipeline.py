import unittest
import numpy as np
import os
import shutil
import pandas as pd

from src.preprocess import preprocess_image, extract_hog_features
from src.disease_info import DISEASE_INFO
from src.history import save_prediction, REPORT_FILE, REPORT_DIR

class PipelineTests(unittest.TestCase):
    def setUp(self):
        # Backup history if it exists
        self.backup_history = False
        self.backup_path = REPORT_FILE + ".bak"
        if os.path.exists(REPORT_FILE):
            shutil.copy(REPORT_FILE, self.backup_path)
            self.backup_history = True
            os.remove(REPORT_FILE)

    def tearDown(self):
        # Restore backup if it exists
        if os.path.exists(REPORT_FILE):
            os.remove(REPORT_FILE)
        if self.backup_history:
            shutil.move(self.backup_path, REPORT_FILE)

    def test_preprocessing(self):
        # Create a dummy BGR image (100x200x3)
        image = np.random.randint(0, 256, (100, 200, 3), dtype=np.uint8)
        processed = preprocess_image(image, size=128)
        
        # Output should be (128, 128)
        self.assertEqual(processed.shape, (128, 128))
        # Pixels should be normalized between 0.0 and 1.0
        self.assertTrue(processed.min() >= 0.0)
        self.assertTrue(processed.max() <= 1.0)

    def test_hog_feature_extraction(self):
        # Grayscale image (128x128)
        gray_image = np.random.rand(128, 128)
        features = extract_hog_features(gray_image)
        
        # Check feature dimension (for 128x128, orientations=9, 8x8 cells, 2x2 blocks)
        # (16-1) * (16-1) * 4 * 9 = 15 * 15 * 36 = 8100 features
        self.assertEqual(features.shape, (8100,))

    def test_disease_info_mappings(self):
        expected_diseases = [
            "Melanoma",
            "Melanocytic Nevi",
            "Benign Keratosis",
            "Basal Cell Carcinoma",
            "Actinic Keratosis",
            "Vascular Lesion",
            "Dermatofibroma"
        ]
        for disease in expected_diseases:
            self.assertIn(disease, DISEASE_INFO)
            self.assertIn("description", DISEASE_INFO[disease])
            self.assertIn("precautions", DISEASE_INFO[disease])
            self.assertTrue(len(DISEASE_INFO[disease]["precautions"]) > 0)

    def test_prediction_history_saving(self):
        # Verify history saving appends to CSV
        success = save_prediction("test_image.jpg", "Melanoma", 95.4)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(REPORT_FILE))
        
        # Load CSV and verify row contents
        df = pd.read_csv(REPORT_FILE)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["Image Name"], "test_image.jpg")
        self.assertEqual(df.iloc[0]["Prediction"], "Melanoma")
        self.assertAlmostEqual(float(df.iloc[0]["Confidence (%)"]), 95.40, places=2)

if __name__ == "__main__":
    unittest.main()
