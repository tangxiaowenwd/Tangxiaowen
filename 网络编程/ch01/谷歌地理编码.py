#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 2021/3/28 22:50
# Author  : TangXiaowen

import requests

def geocode(address):
    parameters = {"address":address,"sensor":'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base,params=parameters)
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])

geocode('207 N.Defiance St,Archbold,OH')