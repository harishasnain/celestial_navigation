from PIL import Image
import numpy as np

def load_image(image_path):
    try:
        with Image.open(image_path) as img:
            # Convert image to RGB (3 channels) or L (1 channel for grayscale)
            if img.mode == 'RGB':
                return np.array(img)
            else:
                return np.array(img.convert('L'))
    except Exception as e:
        print(f"Error loading image: {e}")
        return None
