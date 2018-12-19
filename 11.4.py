#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-19.


import ipaddress

net = ipaddress.ip_network("123.45.67.64/27")

print(net)

print(repr(net))

for a in net:
    print(a)

print(net.num_addresses)
