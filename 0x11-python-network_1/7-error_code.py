#!/usr/bin/python3
""" Error code """
import requests
import sys


if __name__ == "__main__":
    """ init variables """
    url = sys.argv[1]

    html = requests.get(url)
    status = html.status_code

    if status == 200:
        print(html.text)
    else:
        print("Error code:", status)
