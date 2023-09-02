#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found
in the header of the response.
"""
from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError

url = argv[1]

try:
    with urlopen(url) as response:
        X_Request_Id = response.headers.get('X-Request-Id')
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)

print(X_Request_Id)
