"""The purpose of this file is to create a dataframe
where each row is a bus stop in the City Of Pittsburgh.
This will be used instead of the alternative, which is
a bus stop being represented by a bus_stop OBJECT instead
of a row in a dataframe, like I will now create."""

import pandas as pd


def create_df():

    df = pd.read_csv('data/paac_stops_1909/PAAC_Stops_1909.csv')
    # Get to the point where we had rid of none used stops
    
    