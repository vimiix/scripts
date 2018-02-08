# coding=utf-8
# python3
# 将十进制阿拉伯数字转换为罗马数字

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    M = ["", "M", "MM", "MMM"];
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
    return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10];

if __name__ == '__main__':
    roman = intToRoman(int(input("输入阿拉伯数字(1~3000):")))
    print('转换后的罗马数字为：', roman)
