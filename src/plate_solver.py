import os
import sys
from PIL import Image

# Add the root directory to the Python path
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

from tetra3.tetra3 import Tetra3

class PlateSolver:
    def __init__(self):
        self.t3 = Tetra3()

    def solve_image(self, image_path):
        with Image.open(image_path) as img:
            solution = self.t3.solve_from_image(img, distortion=[-0.01, 0.01], fov_estimate=53.5, fov_max_error=5)
        
        if solution['RA'] is None:
            raise ValueError("Failed to solve the image")
        
        return {
            'ra': solution['RA'],
            'dec': solution['Dec'],
            'roll': solution['Roll'],
            'fov': solution['FOV'],
            'distortion': solution['distortion'],
            'rmse': solution['RMSE'],
            'matches': solution['Matches'],
            'prob': solution['Prob']
        }
