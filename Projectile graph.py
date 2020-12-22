import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, pi
from Basic_Functions import get_float

# t = 2usin(theta)/g
# r = (u^2)sin(2theta)/g
# h = (u^2)sin^2(theta)/2g

g = 9.8
v = get_float("Initial velocity: ")
h = 0
theta = get_float("Projectile angle in degrees: ") * pi / 180
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
if tf > 0:
    while t < tf+dt:
        horizontal_distance.append(vx * t)
        h = vy * t - 0.5*(g * t ** 2)
        vertical_distance.append(h)
        time.append(t)
        t += dt
else:
    while t > tf-dt:
        horizontal_distance.append(vx * t)
        h = vy * t - 0.5*(g * t ** 2)
        vertical_distance.append(h)
        time.append(t)
        t -= dt

print()
print(f'Time of flight = {round(2 * v * sin(theta) / g, 3)} s')
print(f'Range of projectile = {round((v ** 2) * sin(2 * theta) / g, 3)} m')
print(f'Maximum height = {round((v ** 2) * (sin(theta) ** 2) / (2 * g), 3)} m')

fig, axs = plt.subplots(2)

axs[0].grid(True)
axs[0].plot(horizontal_distance, vertical_distance)
axs[0].set_xlabel("Horizontal diplacement")
axs[0].set_ylabel("Vertical displacement")

axs[1].grid(True)
axs[1].plot(time, vertical_distance, "b--")
axs[1].plot(time, horizontal_distance, "g--")
axs[1].legend(["Vertical displacement", "Horizontal displacement"])
axs[1].set_xlabel("Time")
axs[1].set_ylabel("Displacement")

plt.show()
