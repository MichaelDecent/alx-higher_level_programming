#!/usr/bin/bash
# a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

URL=$1
if [ $# -lt 1 ]; then
    echo "missing parameter: URL"
else
    curl -s -X "DELETE" "$URL"
fi  