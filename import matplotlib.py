import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from shapely.geometry import LineString
# plt.plot()
# plt.show()


def f(x):
    return x ** 2


def sin(x):
    return 5 * np.sin(x)


x = np.linspace(-5, 5, 1000)
y1 = f(x)
y2 = sin(x)

f_x = [[i, f(i)] for i in x]
# print(f_x)
sin_x = [[i, sin(i)] for i in x]
# =======================================================================
fig, ax = plt.subplots()
ax.plot(x, y1, label='f(x)=x**2')
ax.plot(x, y2, label='f(x)=5sin(x)')
ax.set_title('Plotting Functions in Matplotlib', size=14)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 25)
plt.legend()
plt.show()


line1 = LineString(f_x)
line2 = LineString(sin_x)

intersection = line1.intersection(line2)

# plt.plot(*intersection.xy, 'ro')
intersection_x, intersection_y = zip(*intersection.coords.xy)
plt.plot(intersection_x, intersection_y, 'ro')
plt.show()