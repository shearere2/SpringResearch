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
import plotly.express as px

if __name__ == "__main__":
#     #print(df.crs) # Gives Coordinate Reference System
#     df = gpd.read_file('/Users/shearer/Desktop/SpringResearch/data/City_of_Pittsburgh_Neighborhoods/City_of_Pittsburgh_Neighborhoods.shp')
#     stops = gpd.read_file('/Users/shearer/Desktop/SpringResearch/data/Data/PAAC_Stops_1909-shp.zip')

#     burgh = geoplot.polyplot(df,projection=gcrs.AlbersEqualArea(),figsize = (96,72))
#     burgh_stops = geoplot.pointplot(stops, ax=burgh, ).figure
#     burgh_stops.savefig('data/file1.png')


#    #Also, simple note, this automatically shows us a more complicated web map
#     geoplot.webmap(df,projection=gcrs.WebMercator(),figsize=(100,100)).figure.savefig('data/file2.png')


    hoods = pd.read_csv('/Users/shearer/Desktop/SpringResearch/data/City_of_Pittsburgh_Neighborhoods/City_of_Pittsburgh_Neighborhoods.csv')
    geojson = gpd.read_file('/Users/shearer/Desktop/SpringResearch/data/City_of_Pittsburgh_Neighborhoods/City_of_Pittsburgh_Neighborhoods.geojson')

    fig = px.choropleth_mapbox(hoods, geojson=geojson, color="AREA",
                           locations="HOOD", featureidkey="properties.HOOD",
                           center={"lat": 40.440624, "lon": -79.995888},
                           mapbox_style="carto-positron", zoom=9)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    stops = gpd.read_file('/Users/shearer/Desktop/SpringResearch/data/paac_routes_1909/PAAC_Routes_1909.csv')
    # Try to add stops
    fig.add_layer(px.geo_scatter(stops))