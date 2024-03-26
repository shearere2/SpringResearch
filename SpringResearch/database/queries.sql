CREATE TABLE IF NOT EXISTS bus_stops (
    id INTEGER PRIMARY KEY NOT NULL,
    clever_id VARCHAR(10) NOT NULL,
    stop_name VARCHAR(250),
    timepoint INTEGER,
    direction VARCHAR(100),
    routes_served ARRAY,
    routes_count INTEGER,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    mode VARCHAR(100),
    shelter VARCHAR(100),
    stop_type VARCHAR(100)
);