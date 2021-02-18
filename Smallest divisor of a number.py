from math import ceil

def get_integer(msg="Number: "):
    try:
        i = int(input(msg))
    except ValueError:
        print("Invalid Input")
        return get_integer(msg, "Invalid Input")
    else:
        return i


def smallest_divisor(number):
    for i in range(2, ceil(number ** 0.5 + 1)):
        if number % i == 0:
            return i
    return number


while True:
    no = get_integer("Smallest divisor of: ")
    div = smallest_divisor(no)
    print(f"Smallest divisor of {no} is {div}")
    print()
    if input("Wanna quit?(y/n): ") == 'y':
        break
