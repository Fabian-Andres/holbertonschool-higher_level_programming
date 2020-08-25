#!/usr/bin/python3
""" my github """
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    req = requests.get(url, params={'login': username},
                       auth=(username, password))
    data = req.json()
    print(data.get('id'))
