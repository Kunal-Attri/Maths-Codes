import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as ani
from math import pi
plt.style.use('seaborn-pastel')

fig = plt.figure()

ax = plt.axes(xlim=(0, 2 * pi), ylim=(-25, 25))
line, = ax.plot([], [], lw=3)
ax.grid(True)
x = np.linspace(0, 2*pi, 360)
y = np.tan(x)

def init():
    line.set_data(x, y)
    return line,
def animate(i):
    global x, y
    y = np.tan(x - 0.01 * (-i))
    line.set_data(x, y)
    return line,

anim = ani.FuncAnimation(fig, animate, init_func=init, frames=int(2*pi*100), interval=10/(2*pi), blit = True)
plt.show()
