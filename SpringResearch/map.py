# Installed geoplot through terminal, then importing it
import geoplot
import geoplot.crs as gcrs
"""Note, to get geoplot packages installed, I had to open a new geo_env
    and use this environment to install packages, as the normal conda
    environment wouldn't successfully install."""
import pandas as pd
import geopandas as gpd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import pickle



if __name__ == "__main__":
    #print(df.crs) # Gives Coordinate Reference System
    df = gpd.read_file('/Users/shearer/Desktop/SpringResearch/data/City_of_Pittsburgh_Neighborhoods/City_of_Pittsburgh_Neighborhoods.shp')
    stops = gpd.read_file('/Users/shearer/Desktop/SpringResearch/data/Data/paac_stops_1909/PAAC_Stops_1909.shp')

    burgh = geoplot.polyplot(df,projection=gcrs.AlbersEqualArea())
    burgh_stops = geoplot.pointplot(stops, ax=burgh).figure
    burgh_stops.savefig('data/file1.png')

