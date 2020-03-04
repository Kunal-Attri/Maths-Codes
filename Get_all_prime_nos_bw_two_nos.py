from time import time

from Basic_Functions import get_integer, isprime

while True:
    ini_no = get_integer('Initial no: ')
    final_no = get_integer('Final no: ')
    ini_t = time()
    total = 0
    print(f'Prime no.s in range from {ini_no} to {final_no} are: ')
    for i in range(ini_no, final_no + 1):
        if isprime(i) and i != 1:
            print(i)
            total += 1
    if total == 0:
        print('None')
    else:
        print(f"Total = {total}")
    final_t = time()
    print("Time taken = " + str(final_t - ini_t) + " s")
    print('')
