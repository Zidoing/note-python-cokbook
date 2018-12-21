#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2018-12-20.


import hmac

import os


def client_authenticate(connection, secret_key):
    message = connection.recv(32)

    hash = hmac.new(secret_key, message)

    digest = hash.digest()

    connection.send(digest)


def server_authenticate(connection, secret_key):
    message = os.urandom(32)

    connection.send(message)

    hash = hmac.new(secret_key, message)

    digest = hash.digest()

    response = connection.recv(len(digest))

    return hmac.compare_digest(digest, response)



