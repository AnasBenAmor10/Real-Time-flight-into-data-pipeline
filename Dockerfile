# Start from the Bitnami Spark image Spark
FROM bitnami/spark:3.2.4

# Switch to root to install packages
USER root

#install and upgrade pip
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install --upgrade pip && \
    rm -rf /var/lib/apt/lists/*

# Create the checkpoints directories and ensure the non-root user has write access
RUN mkdir -p /opt/bitnami/spark/checkpoints/flight && \
    chown -R 1001:1001 /opt/bitnami/spark/checkpoints
# Switch back to the default user
USER 1001

#CMD ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.4", "/opt/bitnami/spark/pyspark_consumer.py"]