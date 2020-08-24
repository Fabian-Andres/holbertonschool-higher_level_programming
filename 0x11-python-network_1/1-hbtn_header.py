#!/usr/bin/python3
""" hbtn header """
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.headers['X-Request-Id']
        print(header)
