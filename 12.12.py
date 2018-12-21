#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-21.


def countdown(n):
    while n > 0:
        print("T minus", n)

        yield
        n -= 1
    print("blastoff")


def countUp(n):
    x = 0

    while x < n:
        print("count up", x)

        yield
        x += 1


from collections import deque


class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):

        self._task_queue.append(task)

    def run(self):

        while self._task_queue:

            task = self._task_queue.popleft()

            try:
                next(task)
                self._task_queue.append(task)

            except StopIteration:
                pass


sched = TaskScheduler()

sched.new_task(countdown(10))
sched.new_task(countdown(5))
sched.new_task(countUp(15))

sched.run()