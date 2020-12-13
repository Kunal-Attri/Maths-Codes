from math import ceil, cos, pi

while True:
    n = int(input("No of sides: "))
    a = float(input("Each side length: "))
    diagonals = [a]
    d = n - 3

    if d % 2 == 0:
        temp = -1
    else:
        temp = -2

    for i in range(d):
        if i + 1 <= ceil(d / 2):
            value = (diagonals[-1] * cos(pi / n)) + (diagonals[0] * cos((i + 1) * pi / n))
        else:
            value = diagonals[temp]
            temp -= 2
        diagonals.append(round(value, 3))

    for i in range(1, len(diagonals)):
        print(f"Diagonal {i} = {diagonals[i]}")
    print()





























