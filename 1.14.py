#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 15/11/2018.


class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "User({})".format(self.user_id)


users = [User(23), User(3), User(99)]

print(users)
from operator import attrgetter

print(sorted(users, key=lambda u: u.user_id))
print(sorted(users, key=attrgetter("user_id")))
