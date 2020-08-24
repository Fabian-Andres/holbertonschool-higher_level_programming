#!/usr/bin/python3
""" hbtn status """
import urllib.request


if __name__ == "__main__":
    """ comment """
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        html = html.decode('utf-8')
    print(
        "Body response:\n\t- type: %s\n\t- content: %s"
        % (type(html), html)
    )
