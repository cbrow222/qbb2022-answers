#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

data=np.genfromtxt("plink.assoc.linear", dtype=[int, str, int, str, str, int, float, float, float], encoding=None, names = ["Chr", "SNP", "BP", "A1", "Test", "NMISS", "Beta", "Stat", "P"])

cutoff=5
y = -np.log10(data["P"][1:])
x = range(len(y))
x1=[]
x2=[]
y1=[]
y2=[]
for i, value in enumerate(y):
    if value>=5:
        x1.append(x[i])
        y1.append(value)
    else:
        x2.append(x[i])
        y2.append(value)

fig, ax= plt.subplots()
ax.scatter(x1, y1)
ax.scatter(x2,y2)
ax.set_ylabel("-log10(P-value)")
ax.set_xlabel("Genomic location")
plt.savefig("GS451_Manhattan_plot.png")
plt.close(fig)

info=np.genfromtxt("plink.assoc.linear", dtype=None, encoding=None, names = ["Chr", "SNP", "BP", "A1", "Test", "NMISS", "Beta", "Stat", "P"])


max_index=np.argmax(y)
print(max_index)
print(info["SNP"][max_index+1])