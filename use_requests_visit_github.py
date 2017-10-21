#coding=utf-8
__author__ = "Vimiix"

import json
import requests

URL = 'https://api.github.com'

def build_uri(addr):
    return '/'.join([URL, addr])

def request():
    uri = build_uri("users/vimiix")
    print "uri:",uri
    resp = requests.get(uri)
    print resp.text
    print "End request..."


if __name__ == "__main__":
    print "Start request..."
    request()
