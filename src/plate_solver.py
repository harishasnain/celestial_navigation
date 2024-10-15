import os
import sys

# Add the tetra3 directory to the Python path
tetra3_path = "/home/haris/tetra3"
sys.path.append(tetra3_path)

from tetra3 import Tetra3

def solve_plate(image):
    solver = Tetra3()
    
    # Use the relative path to the database within the tetra3 directory
    database_path = os.path.join(tetra3_path, "default_database.npz")
    solver.load_database(database_path)
    
    # Add necessary parameters for solve_from_image method
    result = solver.solve_from_image(image, 
                                     fov_estimate=80,  # Adjust this value based on your camera's field of view
                                     thresh_factor=10, 
                                     min_area=5)
    if result is None:
        return None

    stars = []
    for star in result.stars:
        stars.append({
            'ra': star.ra,
            'dec': star.dec,
            'x': star.x,
            'y': star.y,
            'magnitude': star.mag  # Add magnitude information
        })

    return stars
