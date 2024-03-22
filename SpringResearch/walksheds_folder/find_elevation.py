import requests
import json
from geopy.distance import distance,lonlat
import numpy as np

unit = 0.00027777777777 / 3.0 # 10 meters represented in decimal degrees

def find_elevation(lat:float, long:float) -> float:
    """Find the elevation of a coordinate

    Args:
        lat (float): Latitude
        long (float): Longitude

    Returns:
        float: Elevation in meters
    """
    url = f'https://api.opentopodata.org/v1/ned10m?locations={lat},{long}'
    response = requests.get(url)
    string = response.content.decode()
    file = json.loads(string)
    '''I can be so specific on this return becuase of how
    specific I know the json format will be.'''
    return file['results'][0]['elevation']


def elevation_difference(start:tuple,end:tuple) -> float:
    start_elev = find_elevation(start[0],start[1])
    end_elev = find_elevation(end[0],end[1])

    return end_elev - start_elev # Represents meters that must be walked
#                                  uphill to get from point 1 to point 2

# FIRST TASK work out cumulative uphill travel between 2 points.
# MAYBE WORK TOWARDS WEBSITE WITH 2 FIELDS AND BUTTON FOR 

def summarize_journey(start:tuple,end:tuple) -> dict:
    """Summarize a linear journey between two coordinates
    (assumed that coordinates are linear from each other)

    Args:
        start (tuple): Starting coordinates
        end (tuple): Ending coordinates

    Returns:
        dict: Dictionary containing the following information:
        Cumulative uphill travel, cumulative downhill travel,
        total distance, total altitude change
    """
    dist = float(distance(lonlat(*start), lonlat(*end)).meters)
    alt = float(elevation_difference(start,end))
    increments = ((dist%10.0)*unit) # Represents number of 10 meter increments between points
    uphill = 0; downhill = 0
    hyp_slope = (start[0] - end[0]) / (start[1] - end[1])
    y_intercept = start[0] - (hyp_slope * start[1])
    lat_line = np.arange(start[0],end[0],increments,dtype=float) # Doesn't include end[0]
    lon_line = np.arange(start[1],end[1],increments,dtype=float) # ^^^^^

    if len(lat_line) == 0: ratio = float(len(lon_line))
    else: ratio = float(len(lon_line)) / float(len(lat_line))
    print()
    if ratio < 0:
        i = lon_line[0]
        j = lon_line[-1]
        lon_line = []
        print()
        lon_line = np.arange(i,j,ratio*increments)
    elif ratio > 0:
        i = start[0]
        j = end[0]
        lat_line = []
        lat_line = np.arange(i,j,(1.0/ratio)*increments) # Should flip the ratio, why doesn't it?

    # Current issue: Need latline and lonline to be same length. How?
    print()






    return {"Cumulative Uphill Travel":None,"Cumulative Downhill Travel":None,
            "Total Distance":dist,"Total Altitude Change":None}

def linked_summary():
    """Summarize a journey that isn't a straight line
    """
    return

if __name__ == "__main__":
    #change = elevation_difference((40,-79.8),(40.01,-79.9))
    #print(f'To get from point one to point two, you will have to go up {change} meters')

    summarize_journey((40.4473,-80.0002),(40.444,-79.9974))