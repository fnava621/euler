from itertools import permutations
import string, time

start = time.time()

def lexi_perm():
    dig = string.digits
    return ''.join(list(permutations(dig))[1000000-1])



num = lexi_perm()

elapsed = time.time() - start

print "%s is the millionth lexicographic perm found in %s sec" % (num, elapsed)

