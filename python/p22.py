import string, time

start = time.time()


def names_scores():
    alphabet = string.uppercase
    s = {alphabet[x]: x+1 for x in range(26)}
    f = open('names.txt').read().replace('"','').replace("\n", '').split(',')

    total = 0
    for rank, name in enumerate(sorted(f), 1):
        sum_name= sum([s[letter] for letter in list(name)])
        total = total + sum_name*rank

    return total

total = names_scores()
elapsed = time.time() - start

print "%s found in %s seconds" % (total,elapsed)
