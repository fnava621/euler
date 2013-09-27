from itertools import count


def smallest_mul(x, y):
    lst = range(x, y+1)
    for num in count(2520, 2520):
        if all(num % x == 0 for x in lst):
            smallest = num
            break

    print smallest
        

if __name__ == '__main__':
    answer = smallest_mul(1,20)
    print answer
