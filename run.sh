#!/bin/bash

#Create a index 

python3 create_index_elastic.py

#Command run
docker-compose exec spark-master spark-submit --class consumer --total-executor-cores 4 --executor-memory 2g --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.4,org.elasticsearch:elasticsearch-spark-30_2.12:8.8.2,commons-httpclient:commons-httpclient:3.1 pyspark_consumer.py >out.txt 

echo "Done"
