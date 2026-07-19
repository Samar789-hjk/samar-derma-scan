import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from src.prepare_dataset import load_and_preprocess_dataset

MODELS_DIR = "models"
MODEL_PATH = os.path.join(MODELS_DIR, "best_model.pkl")
ENCODER_PATH = os.path.join(MODELS_DIR, "label_encoder.pkl")

def train_pipeline(max_samples_per_class=150):
    """
    Full training pipeline: load data, encode labels, train RandomForest, and save assets.
    """
    print("--- Starting Model Training Pipeline ---")
    
    # 1. Load data
    features, labels = load_and_preprocess_dataset(max_samples_per_class)
    
    if len(features) == 0:
        print("Error: No features extracted. Cannot train model.")
        return
        
    # 2. Encode labels
    encoder = LabelEncoder()
    encoded_labels = encoder.fit_transform(labels)
    
    # 3. Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        features, encoded_labels, test_size=0.2, random_state=42, stratify=encoded_labels
    )
    
    print(f"Training shape: {X_train.shape}, Testing shape: {X_test.shape}")
    
    # 4. Train RandomForest Classifier
    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(
        n_estimators=10,
        max_depth=5,
        random_state=42,
        n_jobs=-1,
        class_weight="balanced"
    )
    model.fit(X_train, y_train)
    
    # 5. Evaluate on Test Set
    train_acc = model.score(X_train, y_train) * 100
    test_acc = model.score(X_test, y_test) * 100
    print(f"Model Training Accuracy: {train_acc:.2f}%")
    print(f"Model Testing Accuracy: {test_acc:.2f}%")
    
    # 6. Save models
    if not os.path.exists(MODELS_DIR):
        os.makedirs(MODELS_DIR)
        
    print(f"Saving model to {MODEL_PATH}...")
    joblib.dump(model, MODEL_PATH)
    
    print(f"Saving label encoder to {ENCODER_PATH}...")
    joblib.dump(encoder, ENCODER_PATH)
    
    print("--- Training Pipeline Completed Successfully! ---")
    return model, encoder

if __name__ == "__main__":
    train_pipeline()
