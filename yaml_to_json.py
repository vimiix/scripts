#!/usr/bin/python2
#coding=utf-8
'''
usage: yaml_to_json.py [-h] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  input yaml filename(include path)
'''

__author__ = 'Vimiix'

import json
import yaml
import argparse

def yaml_to_json(path):
    with open(path) as f:
        txt=yaml.load(f)
    return json.dumps(txt)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prefix_chars='-+/')
    parser.add_argument("-f", "--file",required=True, help="input yaml filename(include path)")
    args = parser.parse_args()

    json_txt = yaml_to_json(args.file)
    print "Output:", json_txt
    # ...Something to handling with the json data

