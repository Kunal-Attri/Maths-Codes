import matplotlib.pyplot as plt
from Basic_Functions import get_float

print(u"""
A quadratic equation is in the form of ax\u00B2 + bx +c = 0. To plot, please provide a, b, c.
""")
a = get_float("a: ")
b = get_float("b: ")
c = get_float("c: ")

d = (b**2 - (4 * a * c)) ** 0.5
x1 = ((-b) + d)/(2 * a)
x2 = ((-b) - d)/(2 * a)

print(f"Solution to this equation is x = {x1}, {x2}")
l = 2
if x1 <= x2:
    start = x1 - l
    end = x2 + l
else:
    start = x2 - l
    end = x1 + l

resolution = 0.01
x = []
y = []
i = start
while i <= end:
    x.append(i)
    y.append((a * (i ** 2)) + (b * i) + c)
    i += resolution

plt.xlabel("x")
plt.ylabel("")
plt.plot(x, y)
plt.legend([u""+str(a)+"x\u00B2 + " + str(b) + "x + " + str(c)])
plt.grid(True)
plt.show()
