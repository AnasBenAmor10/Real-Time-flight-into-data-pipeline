<h1 align="center">
  <br>
  Real-Time-flight-into-data-pipeline Dashboard
</h1>
<div align="center">
  <h4>
    <a href="#overview">Overview</a> |
    <a href="#data-pipeline-overview">Data Pipeline Overview</a> |
    <a href="#dockerized-environment">Dockerized Environment</a> |
    <a href="#prerequisites">Prerequisites</a>
    <a href="#setup-and-running-instructions">Setup and Running Instructions</a> |
    <a href="#how-to-launch-kibana-dashboard">How to launch kibana dashboard</a> |
    <a href="#final-result">Final result</a> |
  </h4>
</div>
<br>

## Overview

In this project, we will use a real-time flight tracking API, Apache Kafka, ElastichSearch and Kibana to create a real-time Flight-info data pipeline and track the flights in real-time. We will use a high-level architecture and
corresponding configurations that will allow us to create this data pipeline. The end result will be a Kibana dashboard fetching real-time data from ElasticSearch.

## Data Pipeline Overview
Our project pipeline is as follows:
- **Kafka**: Ingests real-time data from airlabs api.
- **Spark**: Processes and analyzes the data.
- **Elasticsearch**: Stores and indexes the processed data.
- **Kibana**: Visualizes insights on an interactive dashboard.


![Pipeline](images/pipeline.png)


## Dockerized Environment

To ensure seamless operation and management, our Real-time-flight-into-data-pipeline is built upon a Dockerized environment, encapsulating each component of the system within its own container. This approach not only fosters a modular architecture, making it easier to update and maintain individual parts without affecting the whole system, but also enhances scalability and fault tolerance. Each service, from Kafka for real-time data ingestion to Kibana for insightful visualizations, operates in an isolated yet interconnected manner through a custom Docker network. This setup not only reflects best practices in container orchestration but also provides a robust, scalable solution for real-time data processing and visualization. By adopting this architecture, users can enjoy a streamlined setup process, predictable behavior across environments, and a flexible system ready to adapt to future needs and improvements.

![Docker Cluster](images/Docker-cluster.png)

## Prerequisites

- Docker Desktop: Ensure Docker Desktop is installed and running on your system.
- Python: Ensure Python is installed for running the Kafka producer script.

## Setup and Running Instructions
1. Start the Docker Containers: 
    ```
    docker-compose up -d
    ```
2. Install Python dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run the Kafka Producer:
    ```
    python kafka_producer_api.py
    ```
4. Execute the Data Processing Scripts:
    - For Windows: `run.bat`
    - For Linux/MacOS: `run.sh`
5. Access Kibana Dashboard at `http://localhost:5601`.
 `

## How to launch kibana dashboard

- Open http://localhost:5601/ in your browser.
- Go to Management>StackManagement>Kibana>Saved Objects
- Import export.ndjson
- Open dashboard

## Final result
- The image is of a flight tracking interface displaying live air traffic. Color-coded icons show different flight statuses—red for scheduled and yellow for en route flights. Hovering over an aircraft icon reveals its flight details, offering an interactive and informative experience.

![Map](images/map.png)

-The image presents a flight heatmap, using a color gradient from blue to red to show varying concentrations of air traffic across the globe, with the most intense areas highlighted in red.

![Heatmap](images/heatmap.png)

-The bar chart shows the U.S. leading the top five countries in air travel, followed by Ireland, the UK, Canada, and Turkey.

![bar-chart](images/horizantalBar.png)

-The image is a donut chart that illustrates the relative market share of several leading airlines, identified by their IATA codes by different colors. The segments vary in size, indicating the proportion of flights each airline operates.

![Pie](images/pie.png)

-The image features a bar chart that ranks aircraft models by their commonality in operation, using their respective ICAO codes for identification. The size of each bar corresponds to how frequently each aircraft model is used, with some models being more common than others.

![Tree-Map](images/TreeMap.png)

-The chart visualizes how an aircraft's average speed typically increases with altitude, with the trend leveling off at higher altitudes.

![line](images/line.png)



## Contributors
<a href="https://github.com/AnasBenAmor10/Real-Time-flight-into-data-pipeline/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=AnasBenAmor10/Real-Time-flight-into-data-pipeline" />
  
</a>
