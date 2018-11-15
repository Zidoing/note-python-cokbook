#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 15/11/2018.


#  this recipe is slow than  setdefault

#  用于排序的字典

rows = [

    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},

]

from operator import itemgetter

from itertools import groupby

rows.sort(key=itemgetter("date"))

print(rows)
print(groupby(rows, itemgetter("date")))

for date, items in groupby(rows, itemgetter("date")):
    print(date, items)
    for i in items:
        print('    ', i)

import time

start = time.time()
print({key: list(val) for key, val in groupby(rows, itemgetter("date"))})
print(time.time() - start)

start = time.time()

data = {}
for row in rows:
    setdefault = data.setdefault(row["date"], [])
    setdefault.append(row)
print(time.time() - start)
