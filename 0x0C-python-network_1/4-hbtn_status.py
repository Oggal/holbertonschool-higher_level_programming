#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import requests


def fetch(url):
    """fetches a URL"""
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))


if __name__ == "__main__":
    fetch('https://intranet.hbtn.io/status')
