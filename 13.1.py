#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-21.


import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')
