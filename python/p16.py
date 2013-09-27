

"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

def pds(x):
    num= pow(2, x)
    return sum(map(int, (list(str(num)))))

