#!/usr/bin/env python
#-*- coding: utf-8 -*-

import hashlib


def main():
    """ SHA256を使ってみる
    """

    hash_hello = hashlib.sha256(b"hello").hexdigest()

    print(hash_hello)


if "__main__" == __name__:

    main()
