#coding=utf-8
'''获取linux系统内存情况'''
__author__ = 'vimiix'

import subprocess
import re

keyDict = {
    "MemTotal":"总内存(单位G)", 
    "MemFree":"剩余内存(单位G)", 
    "MemAvailable":"可用内存(单位G)", 
    "Cached":"缓存内存(单位G)"
    }

def command(cmd):
    p = subprocess.Popen(cmd, shell=True,\
                        stdout=subprocess.PIPE,\
                        stderr=subprocess.STDOUT)
    resultDict = {}
    for line in p.stdout.readlines():
        result = re.split("\s", str(line))
        if result[0][:-1] in keyDict:
            resultDict[keyDict[result[0][:-1]]] = "%.2f" % (int(result[1])/(1024*2))
        return resultDict
if __name__ == "__main__":
    print command("cat /proc/meminfo")
