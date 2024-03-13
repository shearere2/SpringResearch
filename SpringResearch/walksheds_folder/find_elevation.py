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

if __name__ == "__main__":
    lat = float(input('Enter the latitude: '))
    long = float(input('Enter the longitude: '))
    print(f'Elevation at ({lat},{long}): {str(find_elevation(lat,long))} meters above sea level.')