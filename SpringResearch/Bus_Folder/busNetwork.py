import pandas as pd
import busStop
import geopandas as gpd
import shapely
class busNetwork:

    def __init__(self):
        """Initialize stops as the holder of all stops in the network"""
        self._stops = []

    # Mutators
    def add_stop(self,stop:busStop):
        """Add a stop to the network

        Args:
            stop (busStop): stop to be added
        """
        self._stops.append(stop)

    def del_stop(self,stop:busStop):
        """Delete a stop from the network

        Args:
            stop (busStop): stop to be deleted
        """
        self._stops.remove(stop)

    # Accessors
    def get_stops(self) -> list:
        """Returns the list of the stops in the network

        Returns:
            list: all stops within the network
        """
        return self._stops


    def create_city_network(self) -> object:
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
        network = busNetwork() #Initialize busNetwork object

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

        
        # \/ CURRENT WORKING SECTION: FIX THIS PART \/
        """BELOW removes all empty string neighborhood stops.
        (Does not work perfectly yet)"""
        pop_tester = False
        for i in range(len(network._stops)):
            if pop_tester: i -= 1; pop_tester = False
            if i >= len(network._stops):
                break
            elif network._stops[i].get_neighborhood() == "":
                network._stops.pop(i)
                pop_tester = True
        return network
    

if __name__ == "__main__":
    pitt_no_multipolys = busNetwork.create_city_network()
    
    stops = pitt_no_multipolys.get_stops() # Stops within the network.

    print() # Testing point



# WHAT IS NEXT ON MY PLAN:
"""Will then use neighborhoods dataframe to give each row (neighborhood)
a list of busStops"""


