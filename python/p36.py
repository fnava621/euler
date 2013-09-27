



def db_palindrome():
    db_pal = []
    for x in range(1, 1000000):
        if str(x) == str(x)[::-1]:
            if bin(x)[2:] == bin(x)[2:][::-1]:
                db_pal.append(x)
    return sum(db_pal)


if __name__ == '__main__':
    print db_palindrome()
