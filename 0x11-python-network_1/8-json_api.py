#!/usr/bin/python3
""" Post email """
import requests
import sys

if __name__ == "__main__":
    """ init variables """
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = ""

    values = {'q': query}

    """ Sending data """
    html = requests.post(url, data=values)
    data = html.json()

    if len(data) == 0:
        print("No result")
    else:
        for query_id, query_name in data.items():
            if query_id != 'id' and query_name != 'name':
                print("[%s] %s" % (query_id, query_name))
