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
import os

def combined_csv(path: str):
    """Function created to take in a path to a folder with a lot of .csv files,
    and it merges the files on a common column. Credit to
    https://raredogmarketing.com/resources/combining-multiple-csv-files-into-one-file-using-python-step-by-step-guide
    for a majority of this function.

    Args:
        path (str): The folder path
    """
    folder_path = path

    all_files = os.listdir(folder_path)

    # Filter out non-CSV files
    csv_files = [f for f in all_files if f.endswith('.csv')]

    # Create a list to hold the dataframes
    df_list = []

    for csv in csv_files:
        file_path = os.path.join(folder_path, csv)
        try:
            # Try reading the file using default UTF-8 encoding
            df = pd.read_csv(file_path)
            df_list.append(df)
        except UnicodeDecodeError:
            try:
                # If UTF-8 fails, try reading the file using UTF-16 encoding with tab separator
                df = pd.read_csv(file_path, sep='\t', encoding='utf-16')
                df_list.append(df)
            except Exception as e:
                print(f"Could not read file {csv} because of error: {e}")
        except Exception as e:
            print(f"Could not read file {csv} because of error: {e}")

    # Concatenate all data into one DataFrame    
    from functools import reduce
    df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Neighborhood'],
                                            how='outer'),df_list)
    # Save the final result to a new CSV file
    df_merged.to_csv(os.path.join(folder_path, 'combined_file.csv'), index=False)


if __name__ == "__main__":
    # #print(df.crs) # Gives Coordinate Reference System
    # df = gpd.read_file('/Users/shearer/Desktop/SpringResearch/data/City_of_Pittsburgh_Neighborhoods/City_of_Pittsburgh_Neighborhoods.shp')
    # stops = gpd.read_file('/Users/shearer/Desktop/SpringResearch/data/Data/PAAC_Stops_1909-shp.zip')

    # burgh = geoplot.polyplot(df,projection=gcrs.AlbersEqualArea(),figsize = (96,72))
    # burgh_stops = geoplot.pointplot(stops, ax=burgh, ).figure
    # burgh_stops.savefig('data/file1.png')


    # # Also, simple note, this automatically shows us a more complicated web map
    # # geoplot.webmap(df,projection=gcrs.WebMercator(),figsize=(100,100)).figure.savefig('data/file2.png')


    hoods = pd.read_csv('/Users/shearer/Desktop/SpringResearch/data/City_of_Pittsburgh_Neighborhoods/City_of_Pittsburgh_Neighborhoods.csv')
    geojson = gpd.read_file('/Users/shearer/Desktop/SpringResearch/data/City_of_Pittsburgh_Neighborhoods/City_of_Pittsburgh_Neighborhoods.geojson')

    fig = px.choropleth_mapbox(hoods, geojson=geojson, color="AREA",
                           locations="HOOD", featureidkey="properties.HOOD",
                           center={"lat": 40.440624, "lon": -79.995888},
                           mapbox_style="carto-positron", zoom=9)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    # stops = gpd.read_file('/Users/shearer/Desktop/SpringResearch/data/paac_routes_1909/PAAC_Routes_1909.shp')
    # fig.add_trace(px.scatter_geo(stops))
    #fig.show()

    #hood_data = pd.read_csv('/Users/shearer/Desktop/SpringResearch/data/Data/')

    
    path = '/Users/shearer/Desktop/SpringResearch/data/Data/to_combine'
    combined_csv(path)