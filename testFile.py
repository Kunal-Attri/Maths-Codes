from Basic_Functions import isprime
from time import time

a = 0
b = 10000
count = 0
ini = time()
for i in range(a, b):
    if isprime(i):
        count += 1
f = time()

print(f"Total = {count}\nTime taken: {f-ini}")
