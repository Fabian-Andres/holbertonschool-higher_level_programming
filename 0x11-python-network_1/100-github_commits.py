#!/usr/bin/python3
""" github commits """
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/'+owner+'/'+repo+'/commits'

    req = requests.get(url)
    try:
        data = req.json()
        for i in range(0, 10):
            print("%s: %s" % (data[i]['sha'],
                  data[i]['commit']['author']['name']
            ))
    except IndexError:
        pass
