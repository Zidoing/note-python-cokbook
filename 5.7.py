#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 06/12/2018.


import gzip

with gzip.open('1.2.py.gz', 'rt')  as f:
    text = f.read()

    print(text)
