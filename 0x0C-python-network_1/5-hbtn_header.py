#!/usr/bin/python3
"""fetches header value"""
import requests
import sys


def fetch(url):
    """fetches a URL"""
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))



if __name__ == "__main__":
    fetch(sys.argv[1])
