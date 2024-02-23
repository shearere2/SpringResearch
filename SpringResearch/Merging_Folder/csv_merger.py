import pandas as pd
def csv_merge(large: pd.DataFrame, paths: list, new_name: str):
    """Sequentially merges a list of csv files using pd.merge
    and saves to working directory

    Args:
        large (pd.DataFrame): the data frame that will be passed in as the original
        paths (list): list of file paths for the csvs to merge.
    """
    for path in paths:
        df = pd.read_csv(path)
        large = large.merge(df,on = 'Neighborhood', how = 'outer')
        large.to_csv(f'data/{new_name}.csv', index=False)

if __name__ == "__main__":
    pitt = pd.read_csv('data/City_of_Pittsburgh_Neighborhoods/City_of_Pittsburgh_Neighborhoods.csv')   
    pitt = pitt.set_index('Neighborhood')
    path_list = ['data/Data/to_combine/built-environment-conditions.csv',
                'data/Data/to_combine/education-income.csv',
                'data/Data/to_combine/employment.csv',
                'data/Data/to_combine/housing.csv',
                'data/Data/to_combine/land-use-zoning.csv',
                'data/Data/to_combine/natural-environment-conditions.csv',
                'data/Data/to_combine/population-density.csv',
                'data/Data/to_combine/public-safety.csv',
                'data/Data/to_combine/transportation.csv']  
           
    csv_merge(pitt,path_list, 'pitt_neighborhoods_merged')
