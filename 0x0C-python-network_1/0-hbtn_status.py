#!/usr/bin/python3
"""Fetch url"""
import urllib.request


def fetch(url):
    """Fetch url"""
    with urllib.request.urlopen(url) as response:
        res = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode('utf-8')))

if __name__ == "__main__":
    fetch("https://intranet.hbtn.io/status")
