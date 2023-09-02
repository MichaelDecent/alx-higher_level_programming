#!/usr/bin/python3
"""
 a Python script that takes in a URL, sends a request to
 the URL and displays the body of the response.
"""
import requests
from sys import argv


if __name__ == "__main__":

    url = argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
