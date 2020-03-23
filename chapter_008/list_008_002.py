#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import ecdsa
import binascii


def main():
    """ 公開鍵を生成する
    """

    # 32バイトの乱数を生成する
    private_key = os.urandom(32)

    public_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1).verifying_key.to_string()

    # バイナリデータを16進数に変換する
    print(binascii.hexlify(private_key))
    print(binascii.hexlify(public_key))


if "__main__" == __name__:

    main()
