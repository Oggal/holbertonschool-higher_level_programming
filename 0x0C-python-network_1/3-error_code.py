#!/usr/bin/python3
"""Fetch url"""
import urllib.request
import urllib.error
import sys


def error_code(url):
    """takes in a URL, sends request and displays the response"""
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    error_code(sys.argv[1])
