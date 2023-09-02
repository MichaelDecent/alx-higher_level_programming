#!/usr/bin/python3
"""
A Python script that takes 2 arguments to list 10
most recent commits of a repository.
"""
from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: ./script_name.py <repository_name> <owner_username>")
    else:
        repo = argv[1]
        owner = argv[2]
        url = f'https://api.github.com/repos/{owner}/{repo}/commits'

        response = requests.get(url)

        if response.status_code == 200:
            data_array = response.json()
            if isinstance(data_array, list):
                count = 0
                for data in data_array:
                    print(f"{data.get('sha')}: \
                    {data.get('commit')['author']['name']}")
                    count += 1
                    if count == 10:
                        break
            else:
                print("Response does not contain a list of commits.")
        else:
            print(f"Request failed with status code {response.status_code}")
