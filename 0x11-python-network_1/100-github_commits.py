#!/usr/bin/python3
"""
 a Python script that takes 2 arguments in order to solve this challenge
"""
from sys import argv
import requests

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {'since': '2023-09-01T12:50:00Z'}

    response = requests.get(url, params=params)

    data_array = response.json()
    if isinstance(data_array, list):
        count = 0
        for data in data_array:
            print(f"{data.get('sha')}: {data.get('commit')['author']['name']}")
            count += 1
            if count == 10:
                break
