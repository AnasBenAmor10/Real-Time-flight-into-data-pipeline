#import the necessary library
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.functions import from_json , first, col , when , length




schema = StructType([
    # Define the schema for kafka message
    StructField("hex", IntegerType(), True),
    StructField("reg_number", StringType(), True),
    StructField("flag", StringType(), True),
    StructField("position", StructType([
        StructField("lat", DoubleType(), True),
        StructField("lon", DoubleType(), True),
        StructField("alt", DoubleType(), True),
        StructField("dir", DoubleType(), True)
    ]), True),
    StructField("speed", IntegerType(), True),
    StructField("flight_number", IntegerType(), True),
    StructField("flight_icao", StringType(), True),
    StructField("flight_iata", StringType(), True),
    StructField("dep_icao", StringType(), True),
    StructField("dep_iata", StringType(), True),
    StructField("arr_icao", StringType(), True),
    StructField("arr_iata", StringType(), True),
    StructField("airline_icao", StringType(), True),
    StructField("airline_iata", StringType(), True),
    StructField("aircraft_icao", StringType(), True),
    StructField("status", StringType(), True)
    
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
    .option("kafka.bootstrap.servers", 'localhost:9092') \
    .option("subscribe", "flight") \
    .load()

# Deserialize the JSON from the Kafka message
json_df = kafka_data.selectExpr("CAST(value AS STRING)") \
    .select(from_json("value", schema).alias("data")) \
    .select("data.*") \
    .withColumn("hex", when(length("hex") == 6, col("hex")).otherwise(None))

# Print the schema of the DataFrame
json_df.printSchema()



# Add the filter condition to final_result
final_result_filtered = json_df \
    .filter(col("status") != "landed") \
    .drop("flight_icao", "dep_icao", "arr_icao" , "airline_icao")
# Show the data read from Kafka on the console
query = final_result_filtered \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()
#await 
query.awaitTermination()



