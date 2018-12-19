#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-19.


from urllib import request, parse

url = "http://httpbin.org/get"

params = {
    "name1": "value1",
    "name2": "value2",

}

querystring = parse.urlencode(params)

print(querystring)

u = request.urlopen(url + "?" + querystring)


resp = u.read()


print(resp)
