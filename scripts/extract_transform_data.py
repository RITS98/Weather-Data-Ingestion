from config_processor import config_reader
from requests.auth import HTTPBasicAuth
from tabulate import tabulate
from datetime import datetime
import requests
import pandas as pd
import os


config_reader = config_reader(file_path=os.getcwd() + '/config_weather.ini')

API_KEY = config_reader.get_value(section='Weather API', option='API_KEY')
url = 'http://api.weatherapi.com/v1/current.json'


# storing the locations for which data will be fetched in a list
capitals_of_india = [
    "Vizag",        # Andhra Pradesh
    "Itanagar",     # Arunachal Pradesh
    "Guwahati",     # Assam
    "Patna",        # Bihar
    "Raipur",       # Chhattisgarh
    "Panaji",       # Goa
    "Gandhinagar",  # Gujarat
    "Chandigarh",   # Haryana
    "Shimla",       # Himachal Pradesh
    "Ranchi",       # Jharkhand
    "Bengaluru",    # Karnataka
    "Thiruvananthapuram",  # Kerala
    "Bhopal",       # Madhya Pradesh
    "Mumbai",       # Maharashtra
    "Imphal",       # Manipur
    "Shillong",     # Meghalaya
    "Aizawl",       # Mizoram
    "Kohima",       # Nagaland
    "Bhubaneswar",  # Odisha
    "Amritsar",     # Punjab
    "Jaipur",       # Rajasthan
    "Gangtok",      # Sikkim
    "Chennai",      # Tamil Nadu
    "Hyderabad",    # Telangana
    "Agartala",     # Tripura
    "Lucknow",      # Uttar Pradesh
    "Dehradun",     # Uttarakhand
    "Kolkata"       # West Bengal
]


weather_df = pd.DataFrame()
date_time = ''
for loc in capitals_of_india:
    
    # Setting up the parameters for the get request
    params = {
        "key":API_KEY,
        "q":loc
    }
    
    response = requests.get(url=url, params=params)
    data = response.json()
    
    # Extracting relevant data from the response payload
    city = data['location']['name']
    state = data['location']['region']
    country = data['location']['country']
    lat = data['location']['lat']
    lon = data['location']['lon']
    
    date_time = data['current']['last_updated']
    temp_c = data['current']['temp_c']
    temp_f = data['current']['temp_f']
    wind_speed_kph = data['current']['wind_kph']
    humidity = data['current']['humidity']
    uv = data['current']['uv']
    precip_mm = data['current']['precip_mm']
    condition = data['current']['condition']['text']
    
    columns = ['City','State','Country','Latitude','Longitude','Last Updated','Temperature (C)','Temperature (F)', 'Wind Speed (KPH)', 'Humidity', 'UV', 'Precipitaion (MM)','Condition']
    data_list = [[city, state, country, lat, lon, date_time, temp_c, temp_f, wind_speed_kph, humidity, uv, precip_mm, condition]]
    
    # Converting the list to a Dataframe
    df = pd.DataFrame(data=data_list, columns=columns)
    
    # Appending the latest data with the existing dataframe
    weather_df = pd.concat([weather_df, df], ignore_index=True)

print(tabulate(weather_df[['City','State','Country','Latitude','Longitude','Last Updated','Temperature (C)','Temperature (F)', 'Wind Speed (KPH)']], headers='keys', showindex=False))


# Storing the dataframe as csv file
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
weather_df.to_csv(os.getcwd() + f'/data/receivearea/weather_data_{timestamp}.csv', index=False)

