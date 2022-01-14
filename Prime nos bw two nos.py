from Basic_Functions import get_integer, isprime
from time import time

while True:
    ini_no = get_integer('Initial no: ')
    final_no = get_integer('Final no: ')
    
    total = 0
    print(f'Prime no.s in range from {ini_no} to {final_no} are: ')
    a = time()
    for i in range(ini_no, final_no + 1):
        if isprime(i) and i != 1:
            print(i)
            total += 1
    if total == 0:
        print('None')
    else:
        print(f"Total = {total}")
    print(f"Time = {time() - a}\n")
        
    print('')
    if input("Wanna quit?(y/n): ") == 'y':
        break
