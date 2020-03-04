from Basic_Functions import *

print('''This code calculates no of possible permutations. Kindly provide data as n and r
n: total no of items and r: required no. of items''')

while True:
    n = get_integer("n: ")
    r = get_integer('r: ')
    if n - r < 0:
        print('Invalid input, as n can never be less than r')
    else:
        perm = factorial(n) / factorial(n - r)
        print(f'Possible permutations = {perm}')
    print('')
