import os
import glob
import numpy as np
import pandas as pd
from tabulate import tabulate
from sqlalchemy import create_engine
from config_processor import config_reader


# Getting the latest .csv file from the folder
path = os.getcwd() + '/data/receivearea/*.csv'
csv_file_path = glob.glob(path)
latest_file_path = max(csv_file_path, key=os.path.getmtime)

column_names = ['city', 'state', 'country', 'latitude', 'longitude', 'last_updated', 'temp_c', 'temp_f', 'wind_speed', 'humidity', 'uv', 'precipitaion_mm', 'condition']
data_types = {
    'latitude':np.float64,
    'longitude': np.float64,
    'temp_c':np.float64,
    'temp_f':np.float64,
    'wind_speed':np.float64,
    'humidity':np.float64,
    'uv':np.float64,
    'precipitation_mm':np.float64
}
weather_df = pd.read_csv(latest_file_path, names=column_names, header=None, dtype=data_types, skiprows=1, parse_dates=['last_updated'])
print(tabulate(weather_df[['city', 'state', 'country', 'latitude', 'longitude', 'last_updated', 'temp_c', 'temp_f', 'wind_speed']], headers='keys', showindex=False))



config_reader = config_reader(file_path=os.getcwd() + '/config_weather.ini')
db_username = config_reader.get_value(section='Database Credentials', option='username')
db_password = config_reader.get_value(section='Database Credentials', option='password')
db_hostname = config_reader.get_value(section='Database Credentials', option='host')
db_port_num = config_reader.get_value(section='Database Credentials', option='port')
db_database = config_reader.get_value(section='Database Credentials', option='database')


query = 'SELECT * FROM weather'
engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_hostname}:{db_port_num}/{db_database}')

weather_df.to_sql('weather', con=engine, if_exists='append', index=False)

table_data =  pd.read_sql(query, engine)
print(table_data)


# with engine.connect() as conn:
#     weather_df.to_sql('weather', con=conn.connection, if_exists='append', index=False)
#     table_data =  pd.read_sql(query, engine)
#     print(table_data)