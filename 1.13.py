#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 15/11/2018.


rows = [{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter("fname"))
rows_by_uid = sorted(rows, key=itemgetter("uid"))

# rows_by_fname = sorted(rows, key=lambda k: k["fname"])
# rows_by_uid = sorted(rows, key=lambda k: k["uid"])

print(rows_by_fname)
print(rows_by_uid)

a = itemgetter("fname")
