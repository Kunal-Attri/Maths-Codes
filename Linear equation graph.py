import matplotlib.pyplot as plt

print(u"""
A linear equation is in the form of ax + b = 0. To plot, please provide a, b.
""")
a = float(input("a: "))
b = float(input("b: "))

x = -b / a

print(f"Solution to this equation is x = {x}")
l = 5

start = x - l
end = x + l

resolution = 0.01
x = []
y = []
i = start
while i <= end:
    x.append(i)
    y.append((a * i) + b)
    i += resolution

plt.xlabel("x")
plt.ylabel("")
plt.plot(x, y)
plt.legend([u""+str(a)+"x + " + str(b) + " = 0"])
plt.grid(True)
plt.show()
