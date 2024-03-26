import sqlite3

query = '''
CREATE TABLE IF NOT EXISTS bus_stops (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lastname VARCHAR(100) NOT NULL,
    forename VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

conn = sqlite3.connect('data/bus_stops.db')
cursor = conn.cursor()
cursor.execute(query)
record = cursor.fetchall()
print('version is: ', record)

cursor.close()