import os
import joblib
from sklearn.metrics import classification_report, accuracy_score
from src.prepare_dataset import load_and_preprocess_dataset

MODELS_DIR = "models"
MODEL_PATH = os.path.join(MODELS_DIR, "best_model.pkl")
ENCODER_PATH = os.path.join(MODELS_DIR, "label_encoder.pkl")

def evaluate_model(max_samples_per_class=50):
    """
    Evaluates the saved model on a subset of the dataset.
    """
    print("--- Starting Model Evaluation ---")
    
    if not os.path.exists(MODEL_PATH) or not os.path.exists(ENCODER_PATH):
        print(f"Error: Model or Encoder files not found at {MODEL_PATH} / {ENCODER_PATH}. Please train the model first.")
        return
        
    # Load assets
    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
    
    # Load evaluation data
    features, labels = load_and_preprocess_dataset(max_samples_per_class)
    
    if len(features) == 0:
        print("Error: No features found for evaluation.")
        return
        
    # Predict
    y_true = encoder.transform(labels)
    y_pred = model.predict(features)
    
    # Metrics
    acc = accuracy_score(y_true, y_pred) * 100
    print(f"\nOverall Evaluation Accuracy: {acc:.2f}%")
    
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, target_names=encoder.classes_))
    print("--- Model Evaluation Complete ---")

if __name__ == "__main__":
    evaluate_model()
