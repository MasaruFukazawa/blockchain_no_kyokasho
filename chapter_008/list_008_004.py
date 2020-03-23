#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import ecdsa
import binascii


def main():
    """ 圧縮公開鍵を生成する
    """

    # 32バイトの乱数を生成する
    private_key = os.urandom(32)

    public_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1).verifying_key.to_string()

    # y座標を取り出す
    public_key_y = int.from_bytes(public_key[32:], "big")

    # 圧縮公開鍵を生成
    if public_key_y % 2 == 0:
        public_key_compressed = b"\x02" + public_key[:32]
    else:
        public_key_compressed = b"\x03" + public_key[:32]
        
    # バイナリデータを16進数に変換する
    print(binascii.hexlify(private_key))
    print(binascii.hexlify(public_key_compressed))


if "__main__" == __name__:

    main()
