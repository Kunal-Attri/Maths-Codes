from Basic_Functions import *

while True:
    try:
        num = int(input('Number: '))
    except ValueError:
        print('Invalid Input')
    else:
        total = 0
        print('Factors:')
        if isodd(num):
            for i in range(1, num + 1, 2):
                if num % i == 0:
                    print(i)
                    total += 1
        else:
            for i in range(1, num + 1):
                if num % i == 0:
                    print(i)
                    total += 1
        print(f'Total = {total}')
    print()
