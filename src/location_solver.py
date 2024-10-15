from .plate_solver import PlateSolver
from .spherical_trig import calculate_position
from astropy.time import Time

class LocationSolver:
    def __init__(self):
        self.plate_solver = PlateSolver()

    def solve_location(self, image_path, observation_time):
        # Solve the star image
        solution = self.plate_solver.solve_image(image_path)
        
        # Extract star coordinates (using the matched stars)
        if 'matched_stars' in solution:
            star_coords = [(star[0], star[1]) for star in solution['matched_stars']]
        else:
            # Fallback to using the main solved coordinates
            star_coords = [(solution['ra'], solution['dec'])]
        
        # Calculate position based on star coordinates and time
        time = Time(observation_time)
        location = calculate_position(star_coords, time)
        
        return location, solution
