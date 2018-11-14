#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 07/11/2018.


from collections import OrderedDict

d = OrderedDict()

d["foo"] = 1

d["bar"] = 2
d["spam"] = 3
d["grok"] = 4

for key in d:
    print(key, d[key])
