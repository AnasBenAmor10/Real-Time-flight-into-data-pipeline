import requests
from datetime import datetime
import csv
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")
base_url = 'https://airlabs.co/api/v9/'
endpoint = 'flights'
# Url Api
url_with_key = f"{base_url}{endpoint}?api_key={api_key}"
#print(url_with_key)
response = requests.get(url_with_key)

if response.status_code == 200:
    data = response.json()["response"]

    # init data_tuples
    data_tuples = []

    for flight in data:
        # Create data to csv file 
        flight_data = {
            "hex": flight.get('hex', ''),
            "reg_number": flight.get('reg_number', ''),
            "flag": flight.get('flag', ''),
            "lat": flight.get('lat', ''),
            "lng": flight.get('lng', ''),
            "alt": flight.get('alt', ''),
            "dir": flight.get('dir', ''),
            "speed": flight.get('speed', ''),
            "flight_number": flight.get('flight_number', ''),
            "flight_icao": flight.get('flight_icao', ''),
            "flight_iata": flight.get('flight_iata', ''),
            "dep_icao": flight.get('dep_icao', ''),
            "dep_iata": flight.get('dep_iata', ''),
            "arr_icao": flight.get('arr_icao', ''),
            "arr_iata": flight.get('arr_iata', ''),
            "airline_icao": flight.get('airline_icao', ''),
            "airline_iata": flight.get('airline_iata', ''),
            "aircraft_icao": flight.get('aircraft_icao', ''),
            "updated":flight.get('updated',''),
            "status": flight.get('status', ''),
        }

        # Add to data
        data_tuples.append(tuple(flight_data.values()))

    # Save data into CSV file
    csv_filename = 'flight_data.csv'
    with open(csv_filename, 'a', newline='') as file:
        writer = csv.writer(file)

        # write header to csv
        header = list(flight_data.keys())
        writer.writerow(header)

        # write data into csv
        writer.writerows(data_tuples)