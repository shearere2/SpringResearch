import pandas as pd
class busStop:

    def __init__(self, lat:float, lon:float, routes:list):
        self._lat = lat
        self._lon = lon
        self._routes = routes
    
def stop(df:pd.DataFrame) -> pd.DataFrame:
    df['stop'] = str(df['Latitude']) + str(df['Longitude']) + str(df['Routes_ser'])
    return df


if __name__ == "__main__":
    df = pd.read_csv('data/PAAC_Stops_1909.csv')
    df = stop(df)
    
