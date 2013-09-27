
from operator import mul
import time

start = time.time()


def factorial(n):
    lst = [n]
    while n != 1:
        n -=1
        lst.append(n)
    return reduce(mul, lst)

def lattice(grid):
    f = factorial(2*grid)
    f2 = factorial(grid) * factorial(grid)
    return f/f2




elapsed = time.time() - start
 
print "%s found in %s seconds" % (lattice(20),elapsed)







    




