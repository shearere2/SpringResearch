import subprocess
import json

def elevation_finder(lat:float, long:float) -> float:

    file=json.load(subprocess.run([f'curl https://api.opentopodata.org/v1/test-dataset?locations={lat},{long}'], shell=True))
    for key, value in file['results'][0]: # json files are just dictionaries, so this will give us the  
        if key == 'elevation':
            return value
        




# git clone https://github.com/ajnisbet/opentopodata.git
# cd opentopodata
# make build
# make run

# mkdir ./data/ned10m

# Ran strm format file

# make build && make run
# STUCK ON THIS ABOVE STEP, MIGHT HAVE HAD ERRORS IN FIRST STEP THAT CAUSE THIS

# Ran the above to build my opentopo
        

if __name__ == "__main__":
    print(elevation_finder(0,0))