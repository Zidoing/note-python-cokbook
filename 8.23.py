#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 10/12/2018.


import weakref


class Node:

    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)

        child.parent = self


root = Node('parent')

c1 = Node("Child")

root.add_child(c1)
print(c1.parent)

del root

print(c1.parent)


class Data:
    def __del__(self):
        print("Data.__del__")


class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


a = Data()

del a

a = Node()

del a
a = Node()

a.add_child(Node())

del a

import gc

gc.collect()

print("kk")
