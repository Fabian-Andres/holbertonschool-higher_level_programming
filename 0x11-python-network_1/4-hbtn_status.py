#!/usr/bin/python3
""" hbtn status """
import requests


if __name__ == "__main__":
    """ get request """
    html = requests.get('https://intranet.hbtn.io/status')

    print(
        "Body response:\n\t- type: %s\n\t- content: %s"
        % (type(html.text), html.text)
    )
