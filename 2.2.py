#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 27/11/2018.


filename = "spam.txt"

print(filename.endswith(".txt"))

import os

filenames = os.listdir(".")

print(filenames)

print([filename for filename in filenames if filename.endswith((".py", "ea"))])
