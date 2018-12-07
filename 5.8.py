#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 06/12/2018.


from functools import partial



record_size = 32


with open("1.2.py.gz", 'rb') as f:
    records = iter(partial(f.read, record_size), b'')
    for record in records:
        print(record)