import time
from collections import Counter


"""
https://projecteuler.net/problem=14
"""

start = time.time()

def is_even(n):
    if n % 2 == 0: return True
    else: False


def collatz(n):
    if is_even(n): return n / 2
    else: return 3*n + 1


kv = {}


for x in range(3,1000000):
    lst = [x]
    col = collatz(x)


    while col != 1:
        if col in kv:
            kv[x] = len(lst) + kv[col]
            break
        col = collatz(col)
        lst.append(col)

    if col not in kv:
        kv[x] = len(lst)


mx = Counter(kv).most_common(1)
elapsed = (time.time() - start)

print elapsed, mx
