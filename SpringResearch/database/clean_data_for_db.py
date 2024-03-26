import pandas as pd
class StopReader():

    def __init__(self):
        self.df = pd.read_csv('data/paac_stops_1909/PAAC_Stops_1909.csv')
        self._clean

    def to_db(self, con):
        """Send the data to a database via a SQLAlchemy connection"""
        self.df.to_sql('bus_stops',
                       con,
                       if_exists='append',
                       index=False)

    def _clean(self):
        """Returns clean dataframe with renamed columns"""
        self.df = self.df.rename({'Stop_name':'stop_name',
                        'CleverID':'clever_id',
                        'Direction':'direction',
                        'Timepoint':'timepoint',
                        'Routes_ser':'routes_served',
                        'Routes_cou':'routes_count',
                        'Latitude':'latitude',
                        'Longitude':'longitude',
                        'Mode':'mode',
                        'Shelter':'shelter',
                        'Stop_type':'stop_type'})
        self.df = self.df[['stop_name','clever_id','direction','timepoint',
                 'routes_served','routes_count','latitude',
                 'mode','shelter','stop_type']]
