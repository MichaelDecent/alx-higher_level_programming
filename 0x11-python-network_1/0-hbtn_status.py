#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import Request, urlopen

if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'
    url_data = Request(url)

    with urlopen(url_data) as reponse:
        web_page = reponse.read()

    print(f"""Body response:
    \t- type: {type(web_page)}
    \t- content: {web_page}
    \t- utf8 content: {web_page.decode('utf-8')}""")
