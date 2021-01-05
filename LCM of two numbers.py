from Basic_Functions import get_integer, isprime
from math import ceil

def find_lcm(x, y):
    divisors = {}
    i = 2
    while x > 1:
        while x % i == 0:
            if isprime(i):
                divisors[i] = divisors.get(i, 0) + 1
                x /= i
        i += 1
    i = 2
    while y > 1:
        quantity = 0
        while y % i == 0:
            if isprime(i):
                quantity += 1
                y /= i
        if quantity > divisors.get(i, 0):
            divisors[i] = divisors.get(i, 0) + quantity
        i += 1
    lcm = 1
    for key, value in divisors.items():
        lcm *= (key ** value)
    return lcm

while True:
    x = get_integer("First no: ")
    y = get_integer("Second no: ")
    lcm = find_lcm(x, y)
    print(f"LCM of {x}, {y} is {lcm}")
    print()
    if input("Wanna quit?(y/n): ") == "y":
        break

