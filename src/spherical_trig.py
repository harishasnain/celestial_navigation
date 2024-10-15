import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time

def angular_distance(ra1, dec1, ra2, dec2):
    """Calculate angular distance between two points on a sphere."""
    return np.arccos(np.sin(dec1) * np.sin(dec2) + 
                     np.cos(dec1) * np.cos(dec2) * np.cos(ra1 - ra2))

def calculate_position(star_coords, observation_time):
    """Calculate observer's position based on star coordinates and time."""
    # Convert star coordinates to SkyCoord objects
    stars = [SkyCoord(ra=ra*u.degree, dec=dec*u.degree, frame='icrs') for ra, dec in star_coords]
    
    # Create a grid of possible Earth locations
    lats = np.arange(-90, 91, 1)
    lons = np.arange(-180, 181, 1)
    
    best_location = None
    min_error = float('inf')
    
    for lat in lats:
        for lon in lons:
            location = EarthLocation(lat=lat*u.deg, lon=lon*u.deg)
            altaz_frame = AltAz(obstime=observation_time, location=location)
            
            # Calculate altitudes and azimuths for all stars
            calculated_altaz = [star.transform_to(altaz_frame) for star in stars]
            
            # Calculate error between observed and calculated positions
            error = sum(angular_distance(s1.az.rad, s1.alt.rad, s2.az.rad, s2.alt.rad) 
                        for s1, s2 in zip(stars[:-1], stars[1:]))
            
            if error < min_error:
                min_error = error
                best_location = location
    
    return best_location

