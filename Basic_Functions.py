basic_prime = [3, 5, 7, 11, 13, 15, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def get_integer(message="Number: "):
    try:
        i = int(input(message))
    except ValueError:
        print('Invalid Input')
        return get_integer(message)
    else:
        # empty_line()
        return i


def empty_line():
    print(' ')


def into_integer(x, msg='Cannot be converted into a integer'):
    try:
        x = int(x)
    except ValueError:
        print(msg)
    else:
        return x


def isodd(num):
    odd = True
    if num % 2 == 0:
        odd = False
    return odd


def iseven(num):
    even = True
    if num % 2 != 0:
        even = False
    return even


def isprime(num):
    prime = True
    if iseven(num) and num / 2 != 1:
        prime = False
    if isodd(num):
        for i in basic_prime:
            if num % i == 0 and num / i != 1:
                prime = False
        if prime:
            for i in range(101, int(num / 101 + 1), 2):
                if num % i == 0:
                    prime = False
                    break
    return prime
