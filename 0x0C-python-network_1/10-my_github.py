#!/usr/bin/python3
"""Authenticates to Github API and displays user id"""
import requests
import sys


def GetGithubID(usr, pswd):
    """Authenticates to Github API and displays user id"""
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(usr, pswd))
    try:
        print(r.json().get('id'))
    except Exception as e:
        print("None")


if __name__ == "__main__":
    if (len(sys.argv) == 3):
        GetGithubID(sys.argv[1], sys.argv[2])
