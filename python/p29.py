

def disc_pow(x):
    s = set()
    for a in range(2, x+1):
        for b in range(2, x+1):
            s.update([pow(a, b)])
    return s


if __name__ == '__main__':
    print len(disc_pow(100))
