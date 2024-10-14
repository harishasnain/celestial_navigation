import tetra3
from tetra3 import Tetra3

def solve_plate(image):
    solver = Tetra3()
    solver.load_database("path/to/tetra3/database")
    
    result = solver.solve(image)
    if result is None:
        return None

    stars = []
    for star in result.stars:
        stars.append({
            'ra': star.ra,
            'dec': star.dec,
            'x': star.x,
            'y': star.y
        })

    return stars