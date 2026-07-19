import os
import pandas as pd
import numpy as np
import cv2
from src.preprocess import preprocess_image, extract_hog_features

DATA_DIR = "data"
METADATA_PATH = os.path.join(DATA_DIR, "HAM10000_metadata.csv")
PART1_DIR = os.path.join(DATA_DIR, "HAM10000_images_part_1")
PART2_DIR = os.path.join(DATA_DIR, "HAM10000_images_part_2")

def find_image_path(image_id):
    """
    Search for image file in part 1 and part 2 folders.
    """
    filename = f"{image_id}.jpg"
    path1 = os.path.join(PART1_DIR, filename)
    path2 = os.path.join(PART2_DIR, filename)
    
    if os.path.exists(path1):
        return path1
    elif os.path.exists(path2):
        return path2
    return None

def load_and_preprocess_dataset(max_samples_per_class=100):
    """
    Loads metadata, samples balanced subsets per class,
    preprocesses images, and extracts HOG features.
    """
    if not os.path.exists(METADATA_PATH):
        raise FileNotFoundError(f"Metadata file not found at {METADATA_PATH}")
        
    df = pd.read_csv(METADATA_PATH)
    
    # Class mapping for clean display labels
    class_map = {
        'nv': 'Melanocytic Nevi',
        'mel': 'Melanoma',
        'bkl': 'Benign Keratosis',
        'bcc': 'Basal Cell Carcinoma',
        'akiec': 'Actinic Keratosis',
        'vasc': 'Vascular Lesion',
        'df': 'Dermatofibroma'
    }
    
    # Map raw labels to clean class names
    df['clean_label'] = df['dx'].map(class_map)
    
    sampled_dfs = []
    for label, group in df.groupby('clean_label'):
        # Sample up to max_samples_per_class
        n_samples = min(len(group), max_samples_per_class)
        sampled_group = group.sample(n=n_samples, random_state=42)
        sampled_dfs.append(sampled_group)
        
    balanced_df = pd.concat(sampled_dfs).reset_index(drop=True)
    
    print(f"Total metadata records sampled: {len(balanced_df)}")
    print(balanced_df['clean_label'].value_counts())
    
    features = []
    labels = []
    
    processed_count = 0
    for _, row in balanced_df.iterrows():
        img_path = find_image_path(row['image_id'])
        if not img_path:
            continue
            
        img = cv2.imread(img_path)
        if img is None:
            continue
            
        try:
            # Preprocess
            gray_norm = preprocess_image(img)
            # Extract HOG features
            hog_feat = extract_hog_features(gray_norm)
            
            features.append(hog_feat)
            labels.append(row['clean_label'])
            processed_count += 1
            
            if processed_count % 100 == 0:
                print(f"Processed {processed_count} images successfully...")
        except Exception as e:
            print(f"Error processing image {row['image_id']}: {e}")
            
    print(f"Dataset preparation complete. Loaded {len(features)} images successfully.")
    return np.array(features), np.array(labels)
