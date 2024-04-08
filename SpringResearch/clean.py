import pandas as pd
from SpringResearch.elev_app import elev_tools
from ast import literal_eval
def remove_commas(df,row):
    return df[row].fillna(0).astype(str).apply(lambda x: x.replace(',','')).astype(int)

def starts_and_stops(df:pd.DataFrame):
    for i in range(len(df['starts'])):
        for j in range(len(df['starts'][i])):
            try:
                df['starts'][i][j] = literal_eval(df['starts'][i][j])
                df['stops'][i][i] = literal_eval(df['stops'][i][j])
            except:
                pass
    return df


def hilly_score(row:pd.Series) -> float:
    starts = row['starts']; stops = row['stops']
    uphill = 0; downhill = 0; distance = 0
    for i in range(len(starts)):
        temp_info = elev_tools.summarize_journey(starts[i],stops[i])
        uphill = uphill + temp_info['Cumulative Uphill Travel']
        downhill = downhill + temp_info['Cumulative Downhill Travel']
        distance = distance + temp_info['Total Distance']

    return (uphill + downhill) / distance
