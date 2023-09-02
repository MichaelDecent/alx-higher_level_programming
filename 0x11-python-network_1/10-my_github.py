#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':

    url = 'https://api.github.com/user'
    if len(argv) != 3:
        print("Usage: ./[file_name] [username] [paswword]")
        exit(1)

    username = argv[1]
    token = argv[2]
    basic = HTTPBasicAuth(username, token)

    response = requests.get(url, auth=basic)
    print(response.json().get('id'))
