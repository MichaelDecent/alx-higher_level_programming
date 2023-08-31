#!/usr/bin/bash
#  a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

URL=$1

if [ $# -lt 1 ]; then
    echo "missing parameter: URL"
else
    curl -s "$URL" | wc -c
fi