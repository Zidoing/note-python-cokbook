#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 07/12/2018.


class A:
    def spam(self):
        print("A.spam")


class B(A):
    def spam(self):
        print("B.spam")
        super().spam()


class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')


class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')



class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        print('A.__init__')
        super().__init__()

class B(Base):
    def __init__(self):
        print('B.__init__')
        super().__init__()

class C(A,B):
    def __init__(self):
        print('C.__init__')
        super().__init__()  # Only one call to super() here


c = C()
