#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

coords=np.genfromtxt("plink.eigenvec", dtype=None, encoding=None, names = ["samp", "Sample", "PC1","PC2","PC3","PC4","PC5","PC6","PC7","PC8","PC9","PC10"])

fig, ax=plt.subplots()
ax.scatter(coords["PC1"],coords["PC2"])
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
plt.savefig("ex1.png")
plt.close(fig)