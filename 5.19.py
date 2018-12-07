#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 06/12/2018.
import tempfile
import time
from tempfile import TemporaryFile

with TemporaryFile("w+t") as f:
    f.write("hello")
    f.write("word")

    f.seek(0)
    data = f.read()
    print(tempfile.gettempdir())

    print(data)


while True:
    time.sleep(20)
    break




