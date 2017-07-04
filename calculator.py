#coding=utf-8
#
#**************************************
# 文件名:calculator.py
# 功能：实现计算器
#       支持(+ - * / % sin cos tan sqrt)
#       兼容 py2.x 和 py3.x
# 作者：vimiix
#***************************************

import math
import sys

def cal(s):
    func = ['sin', 'cos', 'tan', 'sqrt']

    for i in func:
        if i in s.lower():
            s = s.replace(i, 'math.'+i)

    #print s
    try:
        s = eval(s)
    except ZeroDivisionError:
        print("除数不能为0")
        exit()
    except NameError:
        print("输入的语法有错误")
        exit()

    return s

def main():
    print("\n计算器\n举例: sqrt(（3 + 4）* sin(45))")

    if sys.version_info.major >= 3:
        s = input("\n请输入算式: ")
    else:
        s = raw_input("\n请输入算式: ")

    s = s.replace(' ','')
    print("结果为: " + str(cal(s)))

if __name__ == '__main__':
    main()
