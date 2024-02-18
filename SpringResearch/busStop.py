import pandas as pd
class busStop:

    def __init__(self, lat:float, lon:float, routes:list):
        self._lat = lat
        self._lon = lon
        self._routes = routes
    
def stop(df:pd.DataFrame) -> pd.DataFrame:
    for row in range(len(df)):
        df['stop'] = busStop(df['Latitude'][row], df['Longitude'][row],df['Routes_ser'][row])
    return df


if __name__ == "__main__":
    df = pd.read_csv('data/PAAC_Stops_1909.csv')
    df = df.apply(stop)
    print(df['stop'][1]._lat)
