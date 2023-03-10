#!/usr/bin/python3
"""fetches header value"""
import requests


def postEmail(url, emailadrs):
    """fetches a URL"""
    data = {'email': emailadrs}
    r = requests.post(url, data)
    print(r.text)


if __name__ == "__main__":
    import sys
    postEmail(sys.argv[1], sys.argv[2])
