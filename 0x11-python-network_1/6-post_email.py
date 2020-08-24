#!/usr/bin/python3
""" Post email """
import requests
import sys

if __name__ == "__main__":
    """ init variables """
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}

    """ Setting of data """
    html = requests.post(url, data=values)
    print(html.text)
