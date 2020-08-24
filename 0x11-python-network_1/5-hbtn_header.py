#!/usr/bin/python3
""" hbtn header """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    header_id = req.headers.get('X-Request-Id')
    print(header_id)
