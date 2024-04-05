#import the necessary library
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.functions import from_json , col , when , length


#The structure of the data  received from a Kafka topic 
schema = StructType([
    StructField("hex", StringType(), True),
    StructField("reg_number", StringType(), True),
    StructField("flag", StringType(), True),
    StructField("position", StructType([
        StructField("lat", DoubleType(), True),
        StructField("lon", DoubleType(), True),
    ]), True),
    StructField("alt", DoubleType(), True),
    StructField("dir", DoubleType(), True), 
    StructField("speed", IntegerType(), True),
    StructField("v_speed", IntegerType(), True),
    StructField("flight_number", StringType(), True), 
    StructField("flight_icao", StringType(), True),
    StructField("flight_iata", StringType(), True),
    StructField("dep_icao", StringType(), True),
    StructField("dep_iata", StringType(), True),
    StructField("arr_icao", StringType(), True),
    StructField("arr_iata", StringType(), True),
    StructField("airline_icao", StringType(), True),
    StructField("airline_iata", StringType(), True),
    StructField("aircraft_icao", StringType(), True),
    StructField("status", StringType(), True),
])

# Configuration Spark
spark_conf = SparkConf() \
    .setAppName("flight_consumer") \
    .setMaster("local") \
    .set("spark.executor.memory", "2g") \
    .set("spark.executor.cores", "2")



# Create a SparkSession
spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()

# Set log level to ERROR
spark.sparkContext.setLogLevel("ERROR")

# Read from the Kafka topic 'flight'
kafka_data = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", 'kafka:9092') \
    .option("subscribe", "flight") \
    .load()

# Deserialize the JSON from the Kafka message
json_df = kafka_data.selectExpr("CAST(value AS STRING)") \
    .select(from_json("value", schema).alias("data")) \
    .select("data.*") \
    .withColumn("hex", when(length("hex") == 6, col("hex")).otherwise(None))
# Convert the 'position' field to the correct format for Elasticsearch
json_df = json_df.withColumn("position", struct(col("position.lon"), col("position.lat")))

# Print the schema of the DataFrame
json_df.printSchema()

# Add the filter condition to final_result
final_result_filtered = json_df \
    .filter(col("status") != "landed") \
    .drop("flight_icao", "dep_icao", "arr_icao" , "airline_icao")
# Show the data read from Kafka on the console
#query = final_result_filtered \
    #.writeStream \
    #.outputMode("append") \
    #.format("console") \
    #.start()
filtered_df = final_result_filtered.filter(
    (col("position.lat").isNotNull()) & (col("position.lon").isNotNull())
)

#write the data into elasticsearch
data = filtered_df.writeStream \
    .format("org.elasticsearch.spark.sql") \
    .outputMode("update") \
    .option("es.mapping.id", "reg_number") \
    .option("es.nodes", "elasticsearch") \
    .option("es.port", "9200") \
    .option("es.nodes.wan.only","true") \
    .option("checkpointLocation", "tmp/checkpoint2") \
    .option("es.resource", "flight")\
    .start()
#await 
#query.awaitTermination()
data.awaitTermination()




