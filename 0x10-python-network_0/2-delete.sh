#!/bin/bash
# This script sends a DELETE request to the URL and displays the body of the response

# Check if URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send DELETE request and display the body
curl -sX DELETE "$1"
