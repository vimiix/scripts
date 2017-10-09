#coding=utf-8
'''根据输入的生日计算年龄'''
__author__ = 'Vimiix'

from time import *
def age():
    print "来吧，骚年，输入你的生日（格式0000-00-00）："
    year, month, day = map(int, raw_input().split('-'))
    curtime = gmtime()
    dday = curtime[2]-day
    dmonth = curtime[1]-month
    dyear = curtime[0]-year
    if dday < 0:
        dday = dday + 30
        dmonth = dmonth - 1
        if dmonth < 0:
            dmonth = dmonth + 12
            dyear = dyear - 1
    if dmonth < 0:
        dmonth = dmonth + 12
        dyear = dyear - 1
    print "你已存活了%s年%s月%s天"%(dyear,dmonth,dday)

if __name__ == "__main__":
    age()

