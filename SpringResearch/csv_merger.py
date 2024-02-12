import pandas as pd
def combined_csv(path_list: list):
    pass

if __name__ == "__main__":
    pitt = pd.read_csv('/Users/shearer/Desktop/SpringResearch/data/City_of_Pittsburgh_Neighborhoods/City_of_Pittsburgh_Neighborhoods.csv')   
    pitt = pitt.rename(columns = {'HOOD':'Neighborhood'}).set_index('Neighborhood')

    path_list = ['/Users/shearer/Desktop/SpringResearch/data/Data/to_combine/built-enviornment-conditions.csv',
                '/Users/shearer/Desktop/SpringResearch/data/Data/to_combine/education-income.csv',
                '/Users/shearer/Desktop/SpringResearch/data/Data/to_combine/employment.csv',
                '/Users/shearer/Desktop/SpringResearch/data/Data/to_combine/housing (1).csv',
                '/Users/shearer/Desktop/SpringResearch/data/Data/to_combine/land-use-zoning.csv',
                '/Users/shearer/Desktop/SpringResearch/data/Data/to_combine/natural-environment-conditions.csv',
                '/Users/shearer/Desktop/SpringResearch/data/Data/to_combine/population-density.csv',
                '/Users/shearer/Desktop/SpringResearch/data/Data/to_combine/public-safety.csv',
                '/Users/shearer/Desktop/SpringResearch/data/Data/to_combine/transportation.csv']         
    for path in path_list:
        df = pd.read_csv(path)
        pitt = pitt.merge(df,on = 'Neighborhood', how = 'outer')
        pitt.to_csv('/Users/shearer/Desktop/SpringResearch/data/test1.csv', index=False)
