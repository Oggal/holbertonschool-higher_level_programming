#!/usr/bin/python3
"""Sends a POST request"""
import requests
import sys


def JsonPost():
    """Sends a POST request"""
    url = "http://0.0.0.0:5000/search_user"
    try:
        q = sys.argv[1]
    except Exception as e:
        q = ""
    data = {'q': q}
    req = requests.post(url, data)
    try:
        id = req.json().get('id')
        name = req.json().get('name')
        if id is None or name is None:
            print("No result")
            return
        print("[{}] {}".format(id, name))
    except Exception as e:
        print("Not a valid JSON")


if __name__ == "__main__":
    JsonPost()
