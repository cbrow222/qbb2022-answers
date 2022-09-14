#!usr/bin/env python

import random
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

reads=150000

coverage=[0]*1000000
for i in range(1,150000):
    start=random.randint(0,999901)
    for j in range(0,100):
        coverage[start+j]+=1

x=np.arange(0,30,0.5)
poisson_counts=scipy.stats.poisson.pmf(x,15)*1000000
fig, ax=plt.subplots()
ax.hist(coverage, bins=40)
ax.plot(x, poisson_counts)
ax.set_xlabel("Coverage")
ax.set_ylabel("Frequency")
fig.savefig("ex1-4.png")
plt.close(fig)
print(poisson_counts)
count=0
for k in coverage:
    if k==0:
        count +=1
        
print(count)