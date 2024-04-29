from elasticsearch import Elasticsearch

# Create an Elasticsearch client
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

# Define the index name
index_name = "esflight"

# Check if the Elasticsearch index exists
if es.indices.exists(index=index_name):
    # Delete the index
    es.indices.delete(index=index_name)
    print(f"Index '{index_name}' has been deleted.")
else:
    print(f"Index '{index_name}' does not exist.")


# Define the mapping for Elasticsearch index
mapping = {
    "mappings": {
        "properties": {
         "hex": { "type": "keyword" },
         "reg_number":{"type": "keyword"},
         "flag":{"type":"keyword"},
         "position":{"type":"geo_point"},
         "alt":{"type":"float"},
         "dir":{"type":"float"},
         "speed":{"type":"integer"},
         "v_speed":{"type":"integer"},
         "flight_number":{"type":"keyword"},
         "flight_iata":{"type":"keyword"},
         "dep_iata":{"type":"keyword"},
         "arr_iata":{"type":"keyword"},
         "airline_iata":{"type":"keyword"},
         "aircraft_icao": { "type": "keyword" },
         "status": { "type": "keyword" },
         "type": { "type": "keyword" },
         "arr_pos":{"type":"geo_point"},
         "dep_pos":{"type":"geo_point"},
         "Departure":{"type":"keyword"},
         "Arrival":{"type":"keyword"},

         }
    }
}
# Create the Elasticsearch index with the specified mapping of my data
es.indices.create(index=index_name, body=mapping)