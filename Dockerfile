# Start from the Bitnami Spark image Spark
FROM bitnami/spark:3.2.4

# Switch to root to install packages
USER root

# Update the package list and install python3-pip, curl, telnet, and other utilities
RUN apt-get update && \
    apt-get install -y python3-pip curl telnet && \
    rm -rf /var/lib/apt/lists/*

# Install Scala 2.12
RUN curl -LO https://downloads.lightbend.com/scala/2.12.15/scala-2.12.15.tgz && \
    tar -xzvf scala-2.12.15.tgz -C /opt/ && \
    rm scala-2.12.15.tgz && \
    mv /opt/scala-2.12.15 /opt/scala

# Set up environment variables for Scala
ENV SCALA_HOME /opt/scala
ENV PATH $PATH:$SCALA_HOME/bin

# Create the checkpoints directories and ensure the non-root user has write access
RUN mkdir -p /opt/bitnami/spark/checkpoints/flight && \
    chown -R 1001:1001 /opt/bitnami/spark/checkpoints

<<<<<<< HEAD
=======
# Copy spark file into a container
>>>>>>> 79ff164 (docker file and workflow)
COPY ./pyspark_consumer.py /opt/bitnami/spark/pyspark_consumer.py

RUN mkdir /app
COPY ./create_index_elastic.py /app/reate_index_elastic.py
# Install the Elasticsearch client for Python
RUN pip install elasticsearch==8.8.2

# Copy create index file into app directory into a spark container
COPY ./create_index_elastic.py /opt/bitnami/spark/create_index_elastic.py

# Set permissions for create_index_elastic.py
RUN chown 1001:1001 /opt/bitnami/spark/create_index_elastic.py && \
    chmod +x /opt/bitnami/spark/create_index_elastic.py

# Switch back to the default user
USER 1001

