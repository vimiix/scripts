# coding:utf-8
__author__ = 'vimiix'

def find_M(n):
    """
    找第n个默尼森数。P是素数且M也是素数，
    并且满足等式M=2**P-1，则称M为默尼森数。
    例如，P=5，M=2**P-1=31，5和31都是素数，
    因此31是默尼森数。
    """

    def is_prime(num):
        if num <= 1: 
            return False
        i = 2
        while i*i <= num: 
            if num % i == 0: 
                return False
            i += 1
        return True   
        
    monis_list = []
    p = 1
    while n:
        p += 1
        if is_prime(p):
            m = 2**p - 1
            if is_prime(m):
                monis_list.append({p:m})
                n -= 1
    print(monis_list)
    return monis_list[-1]
            
print(find_M(6))

