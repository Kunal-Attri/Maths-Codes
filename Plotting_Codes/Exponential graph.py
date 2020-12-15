import matplotlib.pyplot as plt
import numpy as np

exp = int(input("Exponential graph of: "))
start = input("Start of graph (Default = 0): ")
end = input("End of graph (Default = 10): ")
if start == "":
    start = 0
else:
    start = int(start)
if end == "":
    end = 10
else:
    end = int(end)
resolution = 0.001
x = []
y = []
i = start
while i <= end:
    x.append(i)
    i += resolution
for i in x:
    y.append(exp ** i)

plt.xlabel("n")
plt.ylabel(u"" + str(exp)+"\u207F")
plt.plot(x, y)
plt.title(u"Graph of "+str(exp)+"\u207F")
plt.grid(True)
plt.show()
