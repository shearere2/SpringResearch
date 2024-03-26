import sqlalchemy
from SpringResearch.database.clean_data_for_db import StopReader

engine = sqlalchemy.create_engine('sqlite:///data/bus_stops.db')
conn = engine.connect()

reader = StopReader()
reader.to_db(conn)