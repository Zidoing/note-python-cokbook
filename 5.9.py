#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 06/12/2018.


import os.path


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb')  as f:
        f.readinto(buf)
    return buf



with open("sample.bin", 'wb') as f:
    f.write(b"Hello World")


buf = read_into_buffer("sample.bin")

print(buf)