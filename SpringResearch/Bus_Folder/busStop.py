import pandas as pd
class busStop:

    def __init__(self, lat:float, lon:float, routes:list, descr:str):
        """Initializes a bus stop

        Args:
            lat (float): latitude
            lon (float): longitude
            routes (list): routes the bus stop services
            descr (str): PRT's location description of the stop
        """        
        self._lat = lat
        self._lon = lon
        self._routes_served = routes
        # self._neighbors = [] # To be added later on
        self._neighborhood = ""
        self._description = descr
        self._active_bool = not routes == []

    """Accessor Methods"""
    def get_coords(self) -> tuple:
        """Get the coordinates of the bus stop
        in the form (Latitude, Longitude), which
        is standard notation

        Returns:
            tuple: (Latitude, Longitude)
        """
        return (self._lon,self._lat)
    
    def get_routes(self) -> list:
        """Returns a list of all routes that
        the bus stop services.

        Returns:
            list: All routes the bus stop services
        """
        return self._routes_served
    
    def get_neighborhood(self) -> str:
        """Returns the neighborhood that the bus stop
        geographically falls within (according to its
        coordinates).

        Returns:
            str: Neighborhood
        """
        return self._neighborhood
    
    def get_description(self) -> str:
        """Returns the description of the bus stop
        given to it by PRT.  This usually comes
        in the form of an intersection, or nearby
        monument.

        Returns:
            str: Description of the bus stop
        """        
        return self._description
    
    def is_active(self) -> bool:
        """Returns a boolean flagging whether or
        not a stop is currently active (currently
        serves at least 1 route)."""
        return self._active_bool

    """Mutator Methods"""
    # def add_neighbor(self, neighbor:str):
    #     """Add a neighbor to the bus stop's neighbors

    #     Args:
    #         neighbor (str): Stop to become neighbor
    #     """
    #     self._neighbors.append(neighbor)

    # def del_neighbor(self, neighbor:str):
    #     """Delete a neighbor from the bus stop's neighbors

    #     Args:
    #         neighbor (str): Stop to remove from neighbors
    #     """
    #     self._neighbors.remove(neighbor)

    def add_route(self, route:str):
        """Add a route for the stop to service

        Args:
            route (str): New route ID
        """
        self._routes_served.append(route)

    def del_route(self, route:str):
        """Delete a route from this stops serviced routes

        Args:
            route (str): Route ID to be removed
        """
        self._routes_served.remove(route)

    def set_neighborhood(self, hood:str):
        """Sets the neighborhood that the busstop is in.
        All functionalities of this are done within the
        busNetwork class's create_network function.

        Args:
            hood (str): Neighborhood the stop falls within
        """
        self._neighborhood = hood

    def set_description(self, desc: str):
        """Sets the locational description of the stop

        Args:
            desc (str): Locational description of the stop
        """
        self._description = desc



if __name__ == "__main__":
    
    print()