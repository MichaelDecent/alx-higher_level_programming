#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found
in the header of the response.
"""
from sys import argv
from urllib.request import urlopen


url = argv[1]
with urlopen(url) as response:
    X_Request_Id = response.headers.get('X-Request-Id')

print(X_Request_Id)
