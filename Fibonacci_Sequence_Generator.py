import time

from Basic_Functions import *

terms = get_integer('No of terms: ')
ini = time.time_ns()
a = 0
b = 1

term = 1
print(b)
while term < terms:
    c = b
    b += a
    a = c
    print(b)
    term += 1
fin = time.time_ns()
print(f'Time taken = {(fin - ini) / 1000000000} seconds')
