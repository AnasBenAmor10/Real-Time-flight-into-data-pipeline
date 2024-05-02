FROM alpine:3.14

# Update and install bash, curl, and jq. Then, clean up the cache to keep the image size small.
RUN apk update && \
    apk add bash curl jq && \
    rm -rf /var/cache/apk/*

# Create the directory where the NDJSON file and script will be placed.
RUN mkdir -p /tmp/load/

# Copy the NDJSON file and the script into the container.
COPY ./export.ndjson /tmp/load/export.ndjson
COPY ./load_ndjson.sh /tmp/load/load_ndjson.sh

# Ensure the script and the NDJSON file are executable.
RUN chmod +x /tmp/load/load_ndjson.sh && \
    chmod 644 /tmp/load/export.ndjson
