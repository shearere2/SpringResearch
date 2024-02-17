import pandas as pd
class busStop:

    def __init__(self, lat:float, lon:float, routes:list):
        self.lat = lat
        self.lon = lon
        self.routes = routes

def make_class(df:pd.DataFrame) -> pd.DataFrame:
    df['stop'] = busStop(df['Latitude'], df['Longitude'],[0,1])

if __name__ == "__main__":
    df = pd.read_csv('data/PAAC_Stops_1909.csv')
    df = df.apply(make_class)
    print(df['stop'])
