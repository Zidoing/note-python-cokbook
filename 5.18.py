#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 06/12/2018.


import os

fd = os.open('1.2.py.gz', os.O_WRONLY | os.O_CREAT)

print(fd)

f = open(fd, 'wt')

f.write("hell")
f.close()
