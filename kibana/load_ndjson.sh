#!/bin/bash

# Kibana URL
KIBANA_URL='http://localhost:5601'
KIBANA_IMPORT_API="$KIBANA_URL/api/saved_objects/_import"
NDJSON_FILE_PATH='../kibana/export.ndjson'

# Wait for Kibana to be ready
until curl -s "$KIBANA_URL" -o /dev/null; do
    echo "Waiting for Kibana..."
    sleep 10
done
echo "Kibana is ready."

# Sleep a little longer to ensure all services are up
sleep 10

# Import the .ndjson file
response=$(curl -s -w "%{http_code}" -o /dev/null -X POST "$KIBANA_IMPORT_API" -H "kbn-xsrf: true" --form file=@"$NDJSON_FILE_PATH")

if [ "$response" -eq 200 ]; then
    echo "Export.ndjson imported successfully."
else
    echo "Failed to import export.ndjson. HTTP response code: $response"
fi
