import pandas as pd
import busStop
import geopandas as gpd
import shapely
class busNetwork:

    def __init__(self):
        self._stops = []

    # Mutators
    def add_stop(self,stop:busStop):
        self._stops.append(stop)
    def del_stop(self,stop:busStop):
        self._stops.remove(stop)

    # Accessors
    def get_stops(self) -> list:
        return self._stops


    def create_network():
        network = busNetwork()
        df = pd.read_csv('data/PAAC_Stops_1909/PAAC_Stops_1909.csv')
        df['stop'] = df.apply(lambda row: busStop.busStop(row['Latitude'],row['Longitude'],row['Routes_ser']), axis=1)
        stops = df['stop']
        for stop in stops: network.add_stop(stop)

        hoods = gpd.read_file('data/pittsburgh_outline.shp')



        # List of Dataframes that will later be concatenated into one large dataframe
        pre_dfs = []

        # Looping over all "rows" in `my_list`
        for item in stops:
            # Generating a shapely geometry
            geometry = shapely.geometry.Point(item.get_coords())
            msg = item.get_description()
            
            # Creating a single-row-DataFrame.
            temp_df = pd.DataFrame({'geometry':[geometry],
                                    'msg':[msg]})
            
            # Appending this single-row-DataFrame to the `pre_dfs` list
            pre_dfs.append(temp_df)

        # Concatenating all the separate dataframes into one big DataFrame
        single_df = pd.concat(pre_dfs, ignore_index=True).reset_index(drop=True)

        # Finally, generating the actual GeoDataFrame that can be manipulated
        geo_df = gpd.GeoDataFrame(single_df,
                                geometry='geometry',
                                crs='epsg:4326')



        for shape in hoods.geometry:
            for stop in geo_df.geometry:
                if stop.within(shape):
                    network[network.find(stop)].set_neighborhood(shape['HOOD'])
# Runs O(nlogn) I think, which takes forever. Needs improved
        return network
    

if __name__ == "__main__":
    pitt = busNetwork.create_network()
    
    stops = pitt._stops
    for stop in stops:
        print(stop.get_neighborhood())


