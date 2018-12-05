#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 27/11/2018.

line = 'asdf fjdk; afed, fjek,asdf,     foo'

import re

split = re.split(r'[;,\s]\s*', line)

print(split)


fields = re.split(r'(;|,|\s)\s*', line)

print(fields)



fields = re.split(r'(?:;|,|\s)\s*', line)

print(fields)