#!/bin/bash
# This script takes a URL as an argument, sends a request, and displays the size of the body in bytes
curl -sL "$1" | wc -c
