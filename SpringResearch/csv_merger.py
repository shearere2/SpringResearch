import pandas as pd
def csv_merge(large: pd.DataFrame, paths: list):
    for path in paths:
        df = pd.read_csv(path)
        large = large.merge(df,on = 'Neighborhood', how = 'outer')
        large.to_csv('data/test1.csv', index=False)

if __name__ == "__main__":
    pitt = pd.read_csv('data/City_of_Pittsburgh_Neighborhoods/City_of_Pittsburgh_Neighborhoods.csv')   
    pitt = pitt.rename(columns = {'HOOD':'Neighborhood'}).set_index('Neighborhood')
    path_list = ['data/Data/to_combine/built-environment-conditions.csv',
                'data/Data/to_combine/education-income.csv',
                'data/Data/to_combine/employment.csv',
                'data/Data/to_combine/housing.csv',
                'data/Data/to_combine/land-use-zoning.csv',
                'data/Data/to_combine/natural-environment-conditions.csv',
                'data/Data/to_combine/population-density.csv',
                'data/Data/to_combine/public-safety.csv',
                'data/Data/to_combine/transportation.csv']  
           
    csv_merge(path_list)
