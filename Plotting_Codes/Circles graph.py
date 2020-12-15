import matplotlib.pyplot as plt
from math import pi, cos, sin

no = int(input("No of circles to plot: "))
while no > 0:
    x = []
    y = []
    
    start = 0
    end = 2 * pi
    i = start
    
    radius = float(input("Radius: "))
    cx, cy = input("Centre coords: ").split()
    cx, cy = float(cx), float(cy)
    resolution = pi / (180)

    while i < end + resolution:
        x.append(cx + radius * cos(i))
        y.append(cy + radius * sin(i))
        i += resolution
    

    plt.grid(True)
    plt.plot(x, y)
    plt.plot(cx, cy, "o")
    no -= 1
plt.title("Circles")
plt.show()
