


#Find the largest palindrome made from the product of two 3-digit numbers.


def lp(digt):
    # largest palindrome
    
    if digt < 1:
        print "Needs to be greater than 1"

    range_of_digits = range(pow(10, digt-1), pow(10, digt))[::-1]
        
    mx = []
    for x in range_of_digits:
        for y in range_of_digits:
            if y <= x and str(x*y) == str(x*y)[::-1]:
                mx.append(x*y)
                
    return max(mx)


if __name__ == '__main__':
    print lp(3)
    

#Answer 906609
