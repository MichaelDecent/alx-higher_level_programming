#!/usr/bin/python3
"""
 a Python script that takes in a URL and an email,
 sends a POST request to the passed URL with the email as a parameter,
 and displays the body of the response (decoded in utf-8)
"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

url = argv[1]
email = argv[2]
values = {'email': email}
data = urlencode(values)
data = data.encode('ascii')
request = Request(url, data)
try:
    with urlopen(request) as response:
        web_page = response.read().decode('utf-8')
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)

print(web_page)
