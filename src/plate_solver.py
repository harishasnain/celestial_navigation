import os
import sys

# Add the tetra3 directory to the Python path
tetra3_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tetra3'))
sys.path.append(tetra3_path)

import tetra3
print(dir(tetra3))  # This will print all attributes of the tetra3 module

class PlateSolver:
    def __init__(self):
        if hasattr(tetra3, 'Tetra3'):
            self.t3 = tetra3.Tetra3()
        else:
            raise AttributeError("tetra3 module does not have Tetra3 attribute. Available attributes: " + str(dir(tetra3)))

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
