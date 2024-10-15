#!/usr/bin/env python3

import sys
import os

# Add the tetra3 directory to the Python path
tetra3_path = "/home/haris/tetra3"
sys.path.append(tetra3_path)

from datetime import datetime
from src.plate_solver import solve_plate
from src.location_calculator import calculate_location
from src.utils import load_image

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 main.py <image_path> <date> <time>")
        sys.exit(1)

    image_path = sys.argv[1]
    date_str = sys.argv[2]
    time_str = sys.argv[3]

    try:
        timestamp = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid date or time format. Use YYYY-MM-DD HH:MM:SS")
        sys.exit(1)

    image = load_image(image_path)
    if image is None:
        print("Failed to load image")
        sys.exit(1)

    stars = solve_plate(image)
    if not stars:
        print("Failed to solve plate")
        sys.exit(1)

    latitude, longitude = calculate_location(stars, timestamp)
    print(f"Estimated location: {latitude:.6f}°, {longitude:.6f}°")

if __name__ == "__main__":
    main()
