import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as ani
from math import pi
plt.style.use('seaborn-pastel')

fig = plt.figure()
a = pi/360

ax = plt.axes(ylim=(-25, 25))
line, = ax.plot([], [], lw=3)
ax.grid(True)
x = [0]
y = np.tan(np.array(x))
plt.legend(["Tangent graph"])
plt.xlabel("x")

def init():
    line.set_data(x, y)
    return line,
def animate(i):
    global x, y
    x.append(x[-1] + a)
    if x[-1] > 2*pi:
        x.pop(0)
    y = np.tan(np.array(x))
    ax.set_xlim(x[0], x[-1])
    line.set_data(x, y)
    return line,

anim = ani.FuncAnimation(fig, animate, init_func=init, frames=360, interval=1)
plt.show()
