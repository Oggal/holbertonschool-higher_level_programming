#!/usr/bin/python3
"""Sends a POST request"""
import requests
import sys


def JsonPost():
    """Sends a POST request"""
    url = "http://6d4d1d93620d.ae068b5a.hbtn-cod.io:5000/search_user"
    try:
        q = sys.argv[1]
    except Exception as e:
        q = ""
    data = {'q': q}
    req = requests.post(url, data)
    try:
        print(req.json())
    except Exception as e:
        print("Not a valid JSON")


if __name__ == "__main__":
    JsonPost()
