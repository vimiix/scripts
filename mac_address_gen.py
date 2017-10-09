#coding=utf-8
'''随机生成mac地址'''
__author__ = 'Vimiix'

import random

def mac_gen():
    rand_items = []
    for _ in range(6):
        rand_items.append("".join(random.sample('0123456789abcdef', 2)))
    mac_addr = ":".join(rand_items)
    return mac_addr

if __name__ == "__main__":
    print mac_gen()


