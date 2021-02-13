def get_float(msg="Number: "):
    try:
        f = float(input(msg))
    except ValueError:
        print('Invalid Input')
        return get_float(msg)
    else:
        return f

while True:
    no = get_float("Square root of: ")
    root = round(no ** 0.5, 4)
    print(f"Square root of {no} is {root}")
    print()
