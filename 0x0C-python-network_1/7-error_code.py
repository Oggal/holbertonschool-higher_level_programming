#!/usr/bin/python3
"""fetches error value"""
import requests


def fetchError(url):
    """fetches error value"""
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)


if __name__ == "__main__":
    import sys
    fetchError(sys.argv[1])
