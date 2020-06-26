import numpy as np
from tqdm import tqdm, trange
import psutil
import matplotlib.pyplot as plt

r = []
theta = []

for x in trange(0,10000):
    if x > 0:
        # check for factors
        for i in range(2, x):
            if (x % i) == 0:
                break
        else:
            r.append(x)
            theta.append(x)


x = y = []

#--------- plot ----------
fig = plt.figure(facecolor=(0, 0, 0), edgecolor='none',dpi = 180)
ax = fig.add_subplot(111, polar=True)
ax.set_facecolor('black')
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.grid(color='none')
c = ax.scatter(theta, r , s = 1 ,c = theta)



plt.show()