#!/usr/bin/python3
"""
 a Python script that takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    if not argv[2]:
        q = ""
    else:
        q = argv[2]

    params = {'q': q}

    response = requests.post(url, params=params)
    if not response.json():
        response.
