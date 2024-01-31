import requests 
from kafka import KafkaProducer
import json
import time
from datetime import datetime
from dotenv import load_dotenv
import os


bootstrap_servers = 'localhost:9092'
# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
# Api airtraffic flight 
load_dotenv()
api_key = os.getenv("api_key")
base_url = 'https://airlabs.co/api/v9/'
endpoint = 'flights'
#Kafka Topic
flight_topic = "flight"

while True:  # Infinite loop for continuous streaming, you may adjust this as needed
    try:
        url = f"{base_url}{endpoint}?api_key={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()['response']

            for line in data:
                position = {
                    'lat': line['lat'],
                    'lon': line['lng'],
                    "alt":line['alt'],
                    "dir":line['dir']
                }

                d = {
                    "hex":line['hex'],
                    "reg_number":line['reg_number'],
                    "flag":line['flag'],
                    "position":position,
                    "speed":line['speed'],
                    "v_speed":line['v_speed'],
                    "flight_number":line['flight_number'],
                    "flight_icao":line['flight_icao'],
                    "flight_iata":line['flight_iata'],
                    "dep_icao":line['dep_icao'],
                    "dep_iata":line['dep_iata'],
                    "arr_icao":line['arr_icao'],
                    "arr_iata":line['arr_iata'],
                    "airline_icao":line['airline_icao'],
                    "airline_iata":line['airline_iata'],
                    "aircraft_icao":line['aircraft_icao'],
                    "updated":line['updated'],
                    "status":line['status'],
                }

                producer.send('flight', value=d)
                print(d)
                time.sleep(1)
                
            
        else:
            print(f'Error: {response.status_code}')
            print(response.text)

    except Exception as e:
        print(f'An error occurred: {str(e)}')

  
    time.sleep(60) 