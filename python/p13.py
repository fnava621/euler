

def large_sum():
    f = open('dig_p13.txt').read().split()
    return str(sum(map(int, f)))[0:10]


