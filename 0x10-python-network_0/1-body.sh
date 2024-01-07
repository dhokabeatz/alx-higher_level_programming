#!/bin/bash
# This script takes in a URL, sends a GET request, and displays the body of the response (only for 200 status code)

URL=$1

# Send GET request and display body only for 200 status code
curl -sI "$URL" | grep "HTTP/1.1 200 OK" && curl -s "$URL"
