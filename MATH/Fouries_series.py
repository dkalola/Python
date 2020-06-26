import random
from itertools import count
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



y = []
t = np.arange(0, 5, 0.0001)

index = count()

def func(i):
    x = (np.sin(np.pi * t * i) / i)
    return x

def animate(i):
    j = (2*next(index)+1)
    y.append(func(j))

    s = 0
    for x in range(0, len(y)):
        s = s + y[x]

    plt.cla()
    plt.plot(s)



ani = FuncAnimation(plt.gcf(), animate, interval=1)

plt.tight_layout()
plt.show()
