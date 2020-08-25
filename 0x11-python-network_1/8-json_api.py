#!/usr/bin/python3
""" Post email """
import requests
import sys

if __name__ == "__main__":
    """ init variables """
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    values = {'q': q}

    """ Sending data """
    html = requests.post(url, data=values)

    try:
        data = html.json()
        if len(data) == 0:
            print("No result")
        else:
            print("[%s] %s" % (data['id'], data['name']))
    except ValueError:
        print("Not a valid JSON")
