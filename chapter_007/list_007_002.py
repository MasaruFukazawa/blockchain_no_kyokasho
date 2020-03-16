#!/usr/bin/env python
#-*- coding: utf-8 -*-

import hashlib


def main():
    """ 2つのフレーズでSHA256を使ってみる
    """

    hash_hello = hashlib.sha256(b"hello").hexdigest()
    hash_hallo = hashlib.sha256(b"hallo").hexdigest()

    print(hash_hello)
    print(hash_hallo)


if "__main__" == __name__:

    main()

