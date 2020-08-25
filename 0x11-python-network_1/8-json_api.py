#!/usr/bin/python3
""" Post email """
import requests
import sys

if __name__ == "__main__":
    """ init variables """
    url = 'http://ff38d7df.hbtn-cod.io:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    values = {'q': q}

    """ Sending data """
    html = requests.post(url, data=values)

    try:
        data = html.json()
    except ValueError:
        print("Not a valid JSON")

    if len(data) == 0:
        print("No result")
    else:
        for query_id, query_name in data.items():
            if query_id != 'id' and query_name != 'name':
                print("[%s] %s" % (query_id, query_name))
