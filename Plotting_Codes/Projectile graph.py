import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, pi
import mplcursors

# t = 2usin(theta)/g
# r = (u^2)sin(2theta)/g
# h = (u^2)sin^2(theta)/2g

g = 9.8
v = float(input("Initial velocity: "))
h = 0
theta = float(input("Projectile angle in degrees: ")) * pi / 180
dx = 0
dy = 0
t = 0
dt = 0.01
vx = v * cos(theta)
vy = v * sin(theta)
tf = 2 * v * sin(theta) / g

horizontal_distance = []
vertical_distance = []
time = []

while t < tf+dt:
    horizontal_distance.append(vx * t)
    h = vy * t - 0.5*(g * t ** 2)
    vertical_distance.append(h)
    time.append(t)
    t += dt

print()
print(f'Time of flight = {round(2 * v * sin(theta) / g, 3)} s')
print(f'Range of projectile = {round((v ** 2) * sin(2 * theta) / g, 3)} m')
print(f'Maximum height = {round((v ** 2) * (sin(theta) ** 2) / (2 * g), 3)} m')

fig, axs = plt.subplots(2)

mplcursors.cursor(hover=True)
axs[0].grid(True)
axs[0].plot(horizontal_distance, vertical_distance)
axs[0].set_xlabel("Horizontal diplacement")
axs[0].set_ylabel("Vertical displacement")
#axs[0].set_title("Vertical distance vs horizontal distance")

#axs[1].xlabel("Time (s)")
#axs[1].ylabel("Distance (m)")
axs[1].grid(True)
axs[1].plot(time, vertical_distance, "b--")
axs[1].plot(time, horizontal_distance, "g--")
axs[1].legend(["Vertical displacement", "Horizontal displacement"])
axs[1].set_xlabel("Time")
axs[1].set_ylabel("Displacement")
#axs[1].set_title("Displacements vs Time")

plt.show()
