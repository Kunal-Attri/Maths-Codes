from math import sqrt
from Basic_Functions import get_float


def euclidean(x1, y1, x2, y2):
    result = sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    return result


def manhattan(x1, y1, x2, y2):
    result = abs(x2 - x1) + abs(y2 - y1)
    return result


print('This code calculates distance between any two points. Provide following data.')
cons = input("Keep one point constant (y/n): ").lower()
if cons == 'y':
    fPoint = input("Constant point coordinates: ").split()
    x1 = float(fPoint[0])
    y1 = float(fPoint[1])
while cons == 'y':
    sPoint = input("\nSecond point: ").split()
    x2 = float(sPoint[0])
    y2 = float(sPoint[1])

    euclideanDist = euclidean(x1, y1, x2, y2)
    manhattanDist = manhattan(x1, y1, x2, y2)
    print(f"Euclidean Distance: {euclideanDist}")
    print(f"Manhattan Distance: {manhattanDist}")

while cons != 'y':
    fPoint = input("\nFirst point coordinates: ").split()
    x1 = float(fPoint[0])
    y1 = float(fPoint[1])

    sPoint = input("Second point: ").split()
    x2 = float(sPoint[0])
    y2 = float(sPoint[1])

    euclideanDist = euclidean(x1, y1, x2, y2)
    manhattanDist = manhattan(x1, y1, x2, y2)
    print(f"Euclidean Distance: {euclideanDist}")
    print(f"Manhattan Distance: {manhattanDist}")
    
