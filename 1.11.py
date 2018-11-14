# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 14/11/2018.
record = '....................100 .......513.25 ..........'
record = '0123456789012345678901234567890123456789012345678901234567890'

cost = int(record[20:32]) * float(record[40:48])

print(cost)

SHARES = slice(20, 32)
PRICE = slice(40, 48)

cost = int(record[SHARES]) * float(record[PRICE])

print(cost)


s = 'HelloWorld'
a = slice(10, 50, 2)

print(a.indices(len(s)))


for i in range(*a.indices(len(s))):
    print(s[i])