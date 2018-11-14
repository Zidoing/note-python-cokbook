#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 06/11/2018.


import heapq

nums = [1, 2, 3, 4, 5, 34, 432, 21, 343, 534, 432, 123]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
    {"name": "IMB", "shares": 100, "price": 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s["price"])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s["price"])

print(cheap)
print(expensive)

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

heap = list(nums)

print(heap)


heapq.heapify(heap)

print(heap)




print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))