#!/bin/bash
# This script takes a URL as an argument, sends a request, and displays the size of the body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
