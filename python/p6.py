def sum_of_squares(x):
    nums = range(1, x+1)
    return sum(map(lambda x: pow(x, 2), nums))

def sum_of_nums(y):
    return pow(sum(range(1, y+1)), 2)

def diff(z):
    return sum_of_nums(z) - sum_of_squares(z)
