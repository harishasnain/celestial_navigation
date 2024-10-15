import os
from datetime import datetime

def get_image_path():
    while True:
        path = input("Enter the path to the star image: ").strip()
        if os.path.isfile(path):
            return path
        print("Invalid file path. Please try again.")

def get_observation_time():
    while True:
        time_str = input("Enter the observation time (YYYY-MM-DD HH:MM:SS): ").strip()
        try:
            return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Invalid time format. Please try again.")

