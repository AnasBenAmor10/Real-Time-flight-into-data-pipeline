from kafka import KafkaProducer

import csv

import time

import json


#function to read csv file
def read_csv(file_path):

    data = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            data.append(row)

    return data

#flight Schema 
flight_schema = {
            "hex":int,
            "reg_number": str,
            "flag": str,
            "lat": float,
            "lng": float,
            "alt": float,
            "dir": float,
            "speed": int,
            "flight_number":int,
            "flight_icao": str,
            "flight_iata": str,
            "dep_icao": str,
            "dep_iata": str,
            "arr_icao":str ,
            "arr_iata":str ,
            "airline_icao": str,
            "airline_iata": str,
            "aircraft_icao": str,
            "status": str,
}

if __name__ == "__main__":

    bootstrap_servers = 'localhost:9092'



    # For Flight data
    flight_data_path = "flight_data.csv"
    #topic name 
    flight_topic = "flight"
    #read csv file using read_csv function
    flight_data = read_csv(flight_data_path)

   

    # Create a Kafka producer

    producer = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=lambda v: json.dumps(v).encode('utf-8'))



    # Send data to Kafka topic
    for line in flight_data:
        # Cast the record_flight values based on the flight_schema
        flight_data_dict = {}
        for key, value in flight_schema.items():
             raw_value = line[key]
             if raw_value != '' :
                flight_data_dict[key] = value(raw_value)
             else:
                flight_data_dict[key] = None


        # Serialize the casted record and send it to Kafka
        producer.send(flight_topic, value=flight_data_dict)
        print(f"Sent message to {flight_topic}: {flight_data_dict}")

        time.sleep(1)

    # Flush and close the producer
    producer.flush()
    producer.close()




