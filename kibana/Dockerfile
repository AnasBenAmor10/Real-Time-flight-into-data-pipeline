FROM alpine:3.6

# Update and install bash and curl. Then, clean up the cache to keep the image size small.
RUN apk update && apk add bash curl && rm -rf /var/cache/apk/*

# Create the directory where the NDJSON file and script will be placed.
RUN mkdir -p /tmp/load/

# Copy the NDJSON file and the script into the container.
COPY ./export.ndjson /tmp/load/export.ndjson
COPY ./load_ndjson.sh /tmp/load/load_ndjson.sh

# Ensure the script and the NDJSON file are executable.
RUN chmod -R 777 /tmp/load/*
