# Real-Time-flight-into-data-pipeline
# Creating a Real-Time Flight-info Data Pipeline with Kafka, Apache Spark, Elasticsearch and Kibana

In this project, we will use a real-time flight tracking API, Apache Kafka, ElastichSearch and Kibana to create a real-time Flight-info data pipeline and track the flights in real-time. We will use a high-level architecture and
corresponding configurations that will allow us to create this data pipeline. The end result will be a Kibana dashboard fetching real-time data from ElasticSearch.

## Pipeline
Our project pipeline is as follows:

![2](https://user-images.githubusercontent.com/80635318/209438588-6f71c44e-c24f-4e80-b8bd-e3168f9bf963.PNG)

## Prerequisites
The following software should be installed on your machine in order to reproduice our work:

- Spark (spark-3.2.4-bin-hadoop3.2)
- Kafka (kafka_2.12-3.6.1)
- ElasticSearch (elasticsearch-8.8.2)
- Kibana (kibana-8.8.2)
- Python 3.9.18
## Steps
###### Get Flight API:
We started by collecting in real-time Flight informations (Aircraft Registration Number,Aircraft Geo-Latitude,Aircraft Geo-Longitude,Aircraft elevation,Flight numbe...) and then we sent them to Kafka for analytics.

###### Kafka Real-Time Producer:
The data is ingested from the flight streaming data API and sent to a kafka topic. You need to run Kafka Server with Zookeeper and create a dedicated topic for data transport.
###### PySpark Streaming:
 In Spark Streaming, Kafka consumer is created that periodically collect data in real time from the kafka topic and send them into an Elasticsearch index.
###### Index flight-info to Elasticsearch:
You need to enable and start Elasticsearch and run it to store the flight-info and their realtime information for further visualization purpose. You can navigate to http://localhost:9200 to check if it's up and running.
###### Kibana for visualization
Kibana is a visualization tool that can explore the data stored in elasticsearch. In our project, instead of directly output the result, we used this visualization tool to visualize the streaming data in a real-time manner.You can navigate to http://localhost:5601 to check if it's up and running.

## How to run
1. Start Elasticsearch

`/bin/elasticsearch `

2. Start Kibana

`/bin/kibana  `

3. Start Zookeeper server by moving into the bin folder of Zookeeper installed directory by using:

`./bin/zookeeper-server-start.sh ./config/zookeeper.properties`

4. Start Kafka server by moving into the bin folder of Kafka installed directory by using:

`./bin/kafka-server-start.sh ./config/server.properties`

5. Run Kafka producer:

`python3 kafka_producer_api.py`

6. Run PySpark consumer with spark-submit:

`spark-submit  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.4,org.elasticsearch:elasticsearch-spark-30_2.12:8.8.2 pyspark_consumer.py `

## How to launch kibana dashboard

- Open http://localhost:5601/ in your browser.
- Go to Management>Kibana>Saved Objects
- Import P2M-Dashbord.ndjson
- Open dashboard

## Final result
