import pandas as pd
"""This file is used to merge the data outputted from csv_merger.py
with the walkability dataframe.  This could become useful if we decide
to look at walkability near bus stops."""
def tract_hood_dict():
    tract_hood:


if __name__ == "__main__":
    df1 = pd.read_csv('data/pitt_neighborhoods_merged.csv',low_memory=False)
    df2 = pd.read_csv('data/walkability.csv',low_memory=False)
    pittsburgh_walkability = csv_merge(df1,df2)
    pittsburgh_walkability.to_csv(f'data/pittsburgh_walkability.csv', index=False)



# DUE TO AN ISSUE WITH THE LINK BETWEEN TRACTS AND NEIGHBORHOODS
    # I WILL BE PAUSING THE WALKABILITY DATAS USAGE
    # this file is temporariliy not in use.