import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin

from Basic_Functions import get_float

start = 0
end = 2 * pi
# resolution = pi / 180
# i = start
theta = np.linspace(start, end, 360)

print("To plot an ellipse please give the values of a and b respectively")
a = get_float("a: ")
b = get_float("b: ")

x = a * np.cos(theta)
y = b * np.sin(theta)

#while i <= end:
#    x.append(a * cos(i))
#    y.append(b * sin(i))
#    i += resolution

plt.title(u"x\u00B2/" + str(a**2) + " + y\u00B2/" + str(b**2) + " = 1")

extra = 0.5
if a < b:
    c = (b**2 - a**2)**0.5
    plt.plot([0, 0], [c, -c], "ro")
    plt.xlim(-b - extra, b + extra)
    plt.ylim(-b - extra, b + extra)
if a > b:
    c = (a**2 - b**2)**0.5
    plt.plot([c, -c], [0, 0], "ro")
    plt.xlim(-a - extra, a + extra)
    plt.ylim(-a - extra, a + extra)


plt.plot(x, y)
plt.grid(True)
plt.show()
