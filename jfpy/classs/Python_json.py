#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import demjson
def main_json():
    data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
    json1 = json.dumps(data)
    print json1

    jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

    text = json.loads(jsonData)
    print text


def encode():
    data = [{'1':1,'2':3}]
    json = demjson.encode(data)
    print json


def show_demjson():
    decode()
    encode()

def decode():
    json1 = '{"a":1,"b":2,"c":3}'
    text = demjson.decode(json1)
    print text

