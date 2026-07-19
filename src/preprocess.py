import cv2
import numpy as np
from skimage.feature import hog

IMAGE_SIZE = 128

def preprocess_image(image, size=IMAGE_SIZE):
    """
    Preprocess image: resize, convert to grayscale, and normalize.
    Supports BGR, RGB, BGRA, or Grayscale inputs.
    """
    if image is None:
        raise ValueError("Input image is None")

    # If already grayscale (2D array)
    if image.ndim == 2:
        gray = image
    # If BGRA (4 channels)
    elif image.shape[-1] == 4:
        gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
    # If BGR/RGB (3 channels)
    else:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize
    resized = cv2.resize(gray, (size, size))
    
    # Normalize to [0, 1]
    normalized = resized / 255.0
    
    return normalized

def extract_hog_features(gray_image):
    """
    Extract Histograms of Oriented Gradients (HOG) features.
    """
    if gray_image is None:
        raise ValueError("Input image for HOG extraction is None")
        
    features = hog(
        gray_image,
        orientations=9,
        pixels_per_cell=(8, 8),
        cells_per_block=(2, 2),
        block_norm="L2-Hys",
    )
    return features
