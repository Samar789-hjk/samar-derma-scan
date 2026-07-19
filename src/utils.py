import cv2
import numpy as np


def load_image(image_file):
    if image_file is None:
        return None

    image_file.seek(0)

    file_bytes = np.asarray(
        bytearray(image_file.read()),
        dtype=np.uint8
    )

    image = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )

    return image


def resize_image(image, size=400):

    h, w = image.shape[:2]

    scale = size / max(h, w)

    width = int(w * scale)

    height = int(h * scale)

    image = cv2.resize(
        image,
        (width, height)
    )

    return image