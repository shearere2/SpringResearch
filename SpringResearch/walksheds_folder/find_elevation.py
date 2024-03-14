import requests
import json

def find_elevation(lat:float, long:float) -> float:
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

if __name__ == "__main__":
    change = elevation_difference((40,-79.8),(40.01,-79.9))
    print(f'To get from point one to point two, you will have to go up {change} meters')