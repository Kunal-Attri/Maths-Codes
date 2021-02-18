from Basic_Functions import get_integer, isprime
from math import ceil

def find_lcm(numbers):
    divisors = {}
    for x in numbers:
        i = 2
        while x > 1:
            quantity = 0
            while x % i == 0:
                if isprime(i):
                    quantity += 1
                    x /= i
            if quantity > divisors.get(i, 0):
                divisors[i] = divisors.get(i, 0) + quantity
            i += 1

    lcm = 1
    for key, value in divisors.items():
        lcm *= (key ** value)
    return lcm


print("""
To calculate LCM of numbers, type the numbers with spaces between them,
like '12 14 8'
""") 
x = input("Numbers: ").split()
n = [int(i) for i in x]
lcm = find_lcm(n)
print(f"LCM of {n} is {lcm}")
print()
input("Press enter to exit...")    
