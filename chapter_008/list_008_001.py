#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import binascii


def main():
    """ 秘密鍵を生成する
    """

    # 32バイトの乱数を生成する
    private_key = os.urandom(32)

    print(private_key)

    # バイナリデータを16進数に変換する
    print(binascii.hexlify(private_key))


if "__main__" == __name__:

    main()

