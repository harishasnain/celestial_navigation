from datetime import datetime
import ephem
from .spherical_trig import angular_distance, spherical_triangle_solve

def calculate_location(stars, timestamp):
    # Select three brightest stars
    selected_stars = sorted(stars, key=lambda s: s['magnitude'])[:3]

    # Calculate angular distances between stars
    distances = [
        angular_distance(selected_stars[0]['ra'], selected_stars[0]['dec'],
                         selected_stars[1]['ra'], selected_stars[1]['dec']),
        angular_distance(selected_stars[1]['ra'], selected_stars[1]['dec'],
                         selected_stars[2]['ra'], selected_stars[2]['dec']),
        angular_distance(selected_stars[2]['ra'], selected_stars[2]['dec'],
                         selected_stars[0]['ra'], selected_stars[0]['dec'])
    ]

    # Use the Greenwich hour angle (GHA) of the first star as a reference
    observer = ephem.Observer()
    observer.date = timestamp
    star = ephem.FixedBody()
    star._ra = selected_stars[0]['ra']
    star._dec = selected_stars[0]['dec']
    star.compute(observer)
    gha = observer.gst - star.ra

    # Solve the celestial triangle
    lat, lon = solve_celestial_triangle(selected_stars[0], gha, distances[0], distances[2])

    return lat, lon

def solve_celestial_triangle(star, gha, distance1, distance2):
    # Convert star coordinates to co-latitude and longitude
    co_lat = 90 - star['dec']
    co_long = star['ra'] - gha

    # Solve the spherical triangle
    c, A, B = spherical_triangle_solve(co_lat, distance1, distance2)

    # Calculate latitude and longitude
    latitude = 90 - c
    longitude = (co_long + A) % 360

    # Adjust longitude to be in the range -180 to 180
    if longitude > 180:
        longitude -= 360

    return latitude, longitude