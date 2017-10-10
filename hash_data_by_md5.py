#coding=utf-8
'''MD5加密字符串'''
__author__ = "vimiix"

import hashlib


def hash_str(s):
    md5 = hashlib.md5()
    md5.update(s)
    return md5.hexdigest()


if __name__ == "__main__":
    s = raw_input("Input a string:")
    print "Result:",hash_str(s)
