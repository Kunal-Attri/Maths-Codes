import time
import math

while True:
    try:
        fact_num = int(input('Factorial of: '))
    except ValueError:
        print('Invalid Input')
    else:
        # fact = 1
        # ini_t = time.time()
        # for i in range(1, fact_num+1):
        #     fact *= i
        # print(f'Factorial: {fact}')
        # f_t = time.time()
        # print(f'Time taken: {f_t-ini_t} s')
        ini_t = time.time()
        fact = math.factorial(fact_num)
        print(f'Factorial: {fact}')
        f_t = time.time()
        print(f'Time taken: {f_t - ini_t} s')
    print()
