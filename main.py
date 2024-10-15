from src.location_solver import LocationSolver
from src.utils import get_image_path, get_observation_time

def main():
    print("Celestial Navigation System")
    print("---------------------------")
    
    image_path = get_image_path()
    observation_time = get_observation_time()
    
    solver = LocationSolver()
    
    try:
        location, plate_solution = solver.solve_location(image_path, observation_time)
        print(f"\nEstimated Location:")
        print(f"Latitude:  {location.lat:.4f}")
        print(f"Longitude: {location.lon:.4f}")
        print(f"\nPlate Solving Results:")
        print(f"RA: {plate_solution['ra']:.4f}")
        print(f"Dec: {plate_solution['dec']:.4f}")
        print(f"Roll: {plate_solution['roll']:.4f}")
        print(f"FOV: {plate_solution['fov']:.4f}")
        print(f"Distortion: {plate_solution['distortion']:.4f}")
        print(f"RMSE: {plate_solution['rmse']:.4f}")
        print(f"Matches: {plate_solution['matches']}")
        print(f"Probability: {plate_solution['prob']:.2e}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
