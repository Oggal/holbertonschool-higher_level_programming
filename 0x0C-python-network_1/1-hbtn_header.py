#!/usr/bin/python3
"""Fetch url"""
import urllib.request
import sys


def getXRequestID(url):
    """Fetch url"""
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))

if __name__ == "__main__":
    getXRequestID(sys.argv[1])
