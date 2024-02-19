import pandas as pd
class busStop:

    def __init__(self, lat:float, lon:float, routes:list):
        self._lat = lat
        self._lon = lon
        self._routes_served = routes
        self._neighbors = []

    """Accessor Methods"""
    def get_coords(self) -> tuple:
        return (self._lat,self._lon)
    def get_routes(self) -> list:
        return self._routes_served

    """Mutator Methods"""
    def add_neighbor(self, neighbor):
        self._neighbors.append(neighbor)
    def del_neighbor(self, neighbor):
        self._neighbors.remove(neighbor)
    def add_route(self, route:str):
        self._routes_served.append(route)
    def del_route(self, route:str):
        self._routes_served.remove(route)



if __name__ == "__main__":

    df = pd.read_csv('data/PAAC_Stops_1909.csv')
    df['stop'] = df.apply(lambda row: busStop(row.Latitude,row.Longitude,row.Routes_ser), axis=1)
    #df.to_csv('data/stop_test.csv')
    print(df['stop'][0].get_coords()[0]) # Latitude of first stop in df