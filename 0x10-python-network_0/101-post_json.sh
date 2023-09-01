#!/bin/bash
# a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sX "POST" -d @json_file -H "Content-Type: application/json" $1
