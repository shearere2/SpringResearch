import pandas as pd
import busStop
class busNetwork:

    def __init__(self):
        self._stops = []

    def add_stop(self,stop:busStop):
        self._stops.append(stop)
    def del_stop(self,stop:busStop):
        self._stops.remove(stop)

    def create_network():
        network = busNetwork()
        df = pd.read_csv('data/PAAC_Stops_1909.csv')
        df['stop'],stops = df.apply(lambda row: busStop(row.Latitude,row.Longitude,row.Routes_ser), axis=1)
        for stop in stops: network.add_stop(stop)
        return network