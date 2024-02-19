import pandas as pd
class busStop:

    def __init__(self, lat:float, lon:float, routes:list):
        self._lat = lat
        self._lon = lon
        self._routes = routes


if __name__ == "__main__":
    df = pd.read_csv('data/PAAC_Stops_1909.csv')
    df['stop'] = busStop(float(df['Latitude']),float(df['Longitude']),list(df['Routes_ser']))
    #df.to_csv('data/stop_test.csv')
    x = df['stop'][2]._lat
    
    print(x)