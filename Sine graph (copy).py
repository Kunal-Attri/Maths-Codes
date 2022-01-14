import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as ani
from math import pi
#plt.style.use('seaborn-pastel')

fig = plt.figure()
a = pi/360

ax = plt.axes(ylim=(-1.5, 1.5))
ax.scatter([], [])
ax.grid(True)
x = [0]
y = np.sin(np.array(x))

import sys
EPSILON = sys.float_info.epsilon
def convert_to_rgb(minval, maxval, val, colors):
    # `colors` is a series of RGB colors delineating a series of
    # adjacent linear color gradients between each pair.

    # Determine where the given value falls proportionality within
    # the range from minval->maxval and scale that fractional value
    # by the total number in the `colors` palette.
    i_f = float(val-minval) / float(maxval-minval) * (len(colors)-1)

    # Determine the lower index of the pair of color indices this
    # value corresponds and its fractional distance between the lower
    # and the upper colors.
    i, f = int(i_f // 1), i_f % 1  # Split into whole & fractional parts.

    # Does it fall exactly on one of the color points?
    if f < EPSILON:
        return colors[i]
    else: # Return a color linearly interpolated in the range between it and 
          # the following one.
        (r1, g1, b1), (r2, g2, b2) = colors[i], colors[i+1]
        return int(r1 + f*(r2-r1)), int(g1 + f*(g2-g1)), int(b1 + f*(b2-b1))

minval, maxval = -1, 1
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]

def init():
    ax.scatter(x, y)
def animate(i):
    global minval, maxval, colors
    global x, y
    x.append(x[-1] + a)
    x1 = x[-1]
    if x[-1] > 2*pi:
        x.pop(0)
    y = np.sin(np.array(x))
    y1 = y[-1]
    temp = y1
    r, g, b = convert_to_rgb(minval, maxval, temp, colors)
    ax.set_xlim(x[0], x[-1])
    ax.scatter(x1, y1, color=(r/255, g/255, b/255))

anim = ani.FuncAnimation(fig, animate, init_func=init, frames=int(360), interval=1)
plt.show()

