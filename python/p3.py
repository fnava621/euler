import time

start = time.time()

def larg_prime():

    n = 600851475143
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return n

p = larg_prime()
elapsed = time.time() - start

print elapsed, p



    
