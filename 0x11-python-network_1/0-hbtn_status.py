#!/usr/bin/python3
""" hbtn status """
import urllib.request


if __name__ == "__main__":
    """ comment """
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    print(
        "Body response:\n\t- type: %s\n\t- content: %s\n\t- utf8 content: %s"
        % (type(html), html, html.decode('utf-8'))
    )
