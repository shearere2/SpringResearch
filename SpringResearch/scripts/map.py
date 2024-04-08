# Installed geoplot through terminal, then importing it
import geoplot
import geoplot.crs as gcrs
import pandas as pd
import geopandas as gpd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import plotly_express as px
from SpringResearch.Bus_Folder import busNetwork, busStop
import shapely
from SpringResearch import clean
from ast import literal_eval

"""This file is where I test map functions.
Most real, used maps will come from within different files."""

if __name__ == "__main__":

    hoods = pd.read_csv('data/Outputs/pitt_neighborhoods_merged.csv')
    hoods['starts'] = hoods['starts'].apply(lambda row: row.split(' , '))
    hoods['stops'] = hoods['stops'].apply(lambda row: row.split(' , '))
    hoods = clean.starts_and_stops(hoods)
    geojson = gpd.read_file('data/City_of_Pittsburgh_Neighborhoods.geojson')

    # hoods['pop2010'] = clean.remove_commas(hoods,'pop2010')
    hoods['hilly_score'] = hoods.apply(clean.hilly_score,axis=1)
    hoods.to_csv('data/Outputs/hilly.csv')
    print()

    # fig = px.choropleth_mapbox(hoods, geojson=geojson, color='hilly_score',
    #                        locations="Neighborhood", featureidkey="properties.HOOD",
    #                        center={"lat": 40.440624, "lon": -79.995888},
    #                        mapbox_style="carto-positron", zoom=9)
    # fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    # fig.show()

    # print(df.crs) # Gives Coordinate Reference System
    # df = gpd.read_file('data/pittsburgh_outline.shp')
    # print()
    # stops = gpd.read_file('data/paac_stops_1909')

    # burgh = geoplot.polyplot(df,projection=gcrs.AlbersEqualArea(),figsize = (60,45))
    # burgh_stops = geoplot.pointplot(stops, ax=burgh).figure
    # burgh_stops.savefig('data/file1.png')
    # Also, simple note, this automatically shows us a more complicated web map
    # geoplot.webmap(df,projection=gcrs.WebMercator(),figsize=(100,100)).figure.savefig('data/file2.png')


    # hoods = pd.read_csv('data/pitt_neighborhoods_merged.csv')
    # geojson = gpd.read_file('data/pitt_neighborhoods_merged.geojson')

    # fig = px.choropleth_mapbox(hoods, geojson=geojson, color="working_population",
    #                        locations="Neighborhood", featureidkey="properties.Neighborhood",
    #                        center={"lat": 40.440624, "lon": -79.995888},
    #                        mapbox_style="carto-positron", zoom=9)
    # fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    # stops = pd.read_csv('/Users/shearer/Desktop/SpringResearch/data/paac_stops_1909/PAAC_Stops_1909.csv')
    # Try to add stops

    # fig.add_scattergeo(px.scatter_geo(stops))
    # fig.show()
