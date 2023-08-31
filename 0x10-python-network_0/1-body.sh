#!/usr/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

URL=$1
if [ $# -lt 1 ]; then
    echo "missing parameter: URL"
else
    curl -sL -X "GET" "$URL"
fi