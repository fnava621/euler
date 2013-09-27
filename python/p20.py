
# https://projecteuler.net/problem=20


from operator import mul

def fact_dig_sum(n):
    lst = [n]
    while n != 1:
        lst.append((n-1))
        n -= 1
        
    fac = reduce(mul, lst)
    
    return sum(map(int, list(str(fac))))

