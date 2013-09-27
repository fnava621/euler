
from operator import add


def self_powers():
    return str(reduce(add, [pow(y, y) for y in xrange(1, 1001)]))[-10:]
