from sqlalchemy import create_engine, MetaData, Table, Column, String, Float
import csv

engine = create_engine('sqlite:///weather_data.db', echo=True)

metadata = MetaData()

# tabela stations
stations = Table(
    'stations', metadata,
    Column('station', String, primary_key=True),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', String),
    Column('country', String),
    Column('state', String)
)

# tabela measurements
measurements = Table(
    'measurements', metadata,
    Column('station', String),
    Column('date', String),
    Column('precip', Float),
    Column('tobs', Float),
)

# Usuwamy tabele
stations.drop(engine, checkfirst=True)
measurements.drop(engine, checkfirst=True)


metadata.create_all(engine)

conn = engine.connect()

# Wstawienie danych do tabeli stations
with open(r'C:\Users\macie\Downloads\clean_stations.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        conn.execute(stations.insert().values(
            station=row['station'],
            latitude=float(row['latitude']),
            longitude=float(row['longitude']),
            elevation=float(row['elevation']),
            name=row['name'],
            country=row['country'],
            state=row['state']
        ))

# Wstawienie danych do tabeli measurements
with open(r'C:\Users\macie\Downloads\clean_measure.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        conn.execute(measurements.insert().values(
            station=row['station'],
            date=row['date'],
            precip=float(row['precip']),
            tobs=float(row['tobs'])
        ))

print("Tabele w bazie danych:", engine.table_names())


result_stations = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print("Stations Table:", result_stations)

result_measurements = conn.execute("SELECT * FROM measurements LIMIT 5").fetchall()
print("Measurements Table:", result_measurements)

