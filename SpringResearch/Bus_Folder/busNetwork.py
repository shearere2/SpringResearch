import pandas as pd
from SpringResearch.Bus_Folder import busStop
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
    



