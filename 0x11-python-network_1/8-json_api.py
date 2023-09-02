#!/usr/bin/python3
"""
 a Python script that takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) > 1:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}

    response = requests.post(url, data=data)

    try:
        json_file = response.json()
        if json_file:
            print(f"[{json_file['id']}] {json_file['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
