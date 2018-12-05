#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 27/11/2018.

from fnmatch import fnmatch, fnmatchcase

print(fnmatch("foo.txt", "*.txt"))
print(fnmatch("foo.txt", "?oo.txt"))
print(fnmatch("Date45.txt", "Date[0-9]*.txt"))

"""
True
True
True
"""