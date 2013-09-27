import time

start = time.time()


def fibonacci_1000():
    fibs = [1,1]
    while len(str(fibs[-1])) != 1000:
        next_fib = fibs[-1] + fibs[-2]
        fibs.append(next_fib)
    return len(fibs)
        
elapsed = time.time()

term = fibonacci_1000()

print "%s found in %s seconds" % (term,elapsed)
