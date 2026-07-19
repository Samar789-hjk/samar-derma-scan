import os
import csv
from datetime import datetime

REPORT_DIR = "reports"
REPORT_FILE = os.path.join(REPORT_DIR, "prediction_history.csv")

def save_prediction(image_name, disease, confidence):
    """
    Saves a prediction record to prediction_history.csv.
    Creates directory and file headers if they don't exist.
    """
    try:
        # Create reports directory if it doesn't exist
        if not os.path.exists(REPORT_DIR):
            os.makedirs(REPORT_DIR)

        # Check if file exists to write headers
        file_exists = os.path.isfile(REPORT_FILE)

        # Record data
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Write to CSV
        with open(REPORT_FILE, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                # Write header
                writer.writerow(["Timestamp", "Image Name", "Prediction", "Confidence (%)"])
            
            # Write prediction row
            writer.writerow([timestamp, image_name, disease, f"{confidence:.2f}"])
        return True
    except Exception as e:
        print(f"Error saving prediction to history: {e}")
        return False
