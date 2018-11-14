#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 06/11/2018.

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)

    for line in lines:
        if pattern in line:
            yield line, previous_lines

        previous_lines.append(line)


deq = deque(maxlen=2)

print(deq)


deq.append(1)
deq.append(2)
deq.append(3)

print(deq)
