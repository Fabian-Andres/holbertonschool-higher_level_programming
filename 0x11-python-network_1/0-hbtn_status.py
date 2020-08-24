#!/usr/bin/python3
""" hbtn status """
import urllib.request


if __name__ == "__main__":
    """ comment """
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print(
            "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8: {}"
            .format(type(html), html, html.decode('utf-8'))
        )
