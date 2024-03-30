import sqlite3
import pandas as pd

def bus_route(route:str) -> dict:

    conn = sqlite3.connect('data/bus_stops.db')
    return pd.read_sql_query('SELECT CleverID,Latitude,Longitude FROM bus_stops WHERE routes_ser LIKE (?);', conn, params=[route])

if __name__ == "__main__":
    
    x = bus_route('14')
    print()