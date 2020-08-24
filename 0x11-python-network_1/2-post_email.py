#!/usr/bin/python3
""" Post email """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    """ init variables """
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}

    """ Setting of data """
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    """ Seting of request """
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
