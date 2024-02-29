import pandas as pd
import shapely
import geopandas as gpd
from SpringResearch.Bus_Folder import busNetwork, busStop
import plotly.express as px
import geoplot

def PRT_busStops(pitt:pd.DataFrame,stops:list) -> pd.DataFrame:
    """Adds a list of stops to each neighborhood (row)

    Args:
        pitt (pd.DataFrame): Pittsburgh neighborhood data
        stops (list): List of busStop objects in their respective neighborhoods

    Returns:
        pd.DataFrame: Dataframe with a row for each neighborhood
        in the city of Pittsburgh, each containing a list of
        busStop objects
    """
    overall_list = []
    for i in range(len(pitt['Neighborhood'])):
        temp = []
        for j in range(len(stops)):
            if stops[j].get_neighborhood() == pitt.loc[i]['Neighborhood']:
                temp.append(stops[j])
        overall_list.append(temp)
    
    pitt['bus_stops'] = overall_list
    pitt['num_stops'] = pitt['bus_stops'].apply(lambda stops: len(stops))


    return pitt
        

def create_city_network() -> object:
        """Creates the bus network within the city of Pittsburgh.
        Please note that all bus stops from outside of the city
        limits but still a part of PRT's network have been
        EXCLUDED.  Additionally, I also currently have to remove
        all bus stops from multipolygon neighborhoods, like
        Lemington-Lincoln-Belmar, unfortunately.

        Returns:
            busNetwork: The cleaned, created city network of
            bus stops.
        """
        network = busNetwork.busNetwork()
        df = pd.read_csv('data/PAAC_Stops_1909/PAAC_Stops_1909.csv')
        df['stop'] = df.apply(lambda row: # New column in df containing busStop object, using other columns
                              busStop.busStop(row['Latitude'],
                                              row['Longitude'],
                                              row['Routes_ser'],
                                              row['Stop_name']), axis=1)
        stops = df['stop'] # Make a series of stops from the bus stops in df
        for stop in stops: network.add_stop(stop) # Add each stop to the network

        hoods = gpd.read_file('data/pittsburgh_outline.shp') # Geopandas df of neighborhoods shapes

        
        """THIS SECTION BELOW IS WHAT CREATES THE COMPARABLE SHAPES AND POINTS"""
        # List of Dataframes that will later be concatenated into one large dataframe
        pre_dfs = []
        for item in stops:
            # Generating a shapely geometry
            geometry = shapely.geometry.Point(item.get_coords())
            msg = item.get_description()
            
            # Creating a single-row-DataFrame.
            temp_df = pd.DataFrame({'geometry':[geometry],
                                    'msg':[msg]})
            
            # Appending this single-row-DataFrame to the `pre_dfs` list
            pre_dfs.append(temp_df)
        
        single_df = pd.concat(pre_dfs, ignore_index=True).reset_index(drop=True)
        geo_df = gpd.GeoDataFrame(single_df,
                                geometry='geometry',
                                crs='epsg:4326')

        """Below is the most important part; this is where a stop
        is given a hood"""

        for i in range(len(hoods)):
            for j in range(len(geo_df)):
                if (hoods.loc[i]['geometry']).contains((geo_df.loc[j].geometry)):
                    network._stops[j].set_neighborhood(hoods.loc[i]['HOOD']) # THIS LINE WORKS CORRECTLY DO NOT MODIFY

        
        """BELOW removes all empty string neighborhood stops."""
        pop_tester = False
        for i in range(len(network._stops)):
            if pop_tester: i -= 1; pop_tester = False
            if i >= len(network._stops):
                break
            elif network._stops[i].get_neighborhood() == "":
                network._stops.pop(i)
                pop_tester = True

        return network


def create() -> pd.DataFrame:

    pitt_no_multipolys = create_city_network()
    stops = pitt_no_multipolys.get_stops()
    new_df = PRT_busStops(pd.read_csv('data/Outputs/pitt_neighborhoods_merged.csv'),
                          stops) # Perfectly gets me the df with the bus stops
    return [new_df,stops]


def map_stops():
    [hoods,stops] = create()
    df = gpd.read_file('data/pittsburgh_outline.shp')
    axis = geoplot.polyplot(df,projection=geoplot.crs.AlbersEqualArea(),figsize = (60,45))

    print()
    geojson = gpd.read_file('data/pittsburgh_outline.shp/City_of_Pittsburgh_Neighborhoods.geojson')

    fig = px.choropleth_mapbox(hoods, geojson=geojson, color='num_stops',
                           locations="Neighborhood", featureidkey="properties.HOOD",
                           center={"lat": 40.440624, "lon": -79.995888},
                           mapbox_style="carto-positron", zoom=9)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


    bus_stops = px.scatter_geo(hoods, ) #stops.lat,stops.lon,)
    fig.add_trace(bus_stops)
    fig.show()


if __name__ == "__main__":
    hoods = create()

