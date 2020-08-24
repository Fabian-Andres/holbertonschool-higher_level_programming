#!/usr/bin/python3
""" Error code """
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    """ init variables """
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
