from Basic_Functions import get_integer

def find_hcf(x, y):
    smaller = x if x < y else y
    for i in range(smaller, 0, -1):
        if (x % i == 0) and (y % i == 0):
            return i
        

while True:
    x = get_integer("First no: ")
    y = get_integer("Second no: ")
    hcf = find_hcf(x, y)
    print(f"HCF of {x}, {y} is {hcf}")
    print()
    if input("Wanna quit?(y/n): ") == 'y':
        break
