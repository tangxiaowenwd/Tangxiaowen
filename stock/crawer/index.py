#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 2021/3/13 19:48
# Author  : TangXiaowen
import requests
from lxml import etree

cookies = "csrftoken=3RKePByFiI2mELbouY1PdbhJD1omsOCAzRWfGvJSXIz42jyNUD6wdJM054a4M4rx; sessionid=c32wx6simcdjasfgiq6qubinkv9fif2u"
cookies_jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(";"):
    key,value = cookie.split("=",1)
    cookies_jar.set(key,value)


url = "http://127.0.0.1:8080/index"

header = {'Content-Length': '',
          'Content-Type': 'text/plain',
          'Host': '127.0.0.1:8080', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
          'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

results = requests.get(url=url,headers=header,cookies=cookies_jar)
print(results.text)

