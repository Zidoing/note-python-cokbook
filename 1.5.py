#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 07/11/2018.


import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        data = heapq.heappop(self._queue)
        return data[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item{!r}'.format(self.name)


q = PriorityQueue()

q.push(Item("foo"), 1)
q.push(Item("bar"), 2)
q.push(Item("spam"), 5)
q.push(Item("grok"), 3)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
