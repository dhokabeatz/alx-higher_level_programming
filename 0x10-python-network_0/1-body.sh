#!/bin/bash
# This script takes in a URL, sends a GET request, and displays the body of the response (only for 200 status code)

URL=$1

# Send GET request and display body only for 200 status code
response=$(curl -sI "$URL")

# Display the entire response for debugging
echo "Response headers:"
echo "$response"

# Check if the status code is 200
if echo "$response" | grep -q "HTTP/1.1 200 OK"; then
    echo "Status code is 200. Sending GET request to $URL"
    body=$(curl -s "$URL")
    echo "Response body:"
    echo "$body"
else
    echo "Status code is not 200. No body will be displayed."
fi
