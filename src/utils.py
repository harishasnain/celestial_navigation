from PIL import Image
import numpy as np

def load_image(image_path):
    try:
        with Image.open(image_path) as img:
            return np.array(img)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None