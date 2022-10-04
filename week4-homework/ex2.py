#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

freq_data=np.genfromtxt("plink.frq", dtype=[int,str,str,str,float,float], encoding=None, names=["Chr", "SNP", "A1","A2","MAF","NCHROBS"])

fig, ax = plt.subplots()
ax.hist(freq_data["MAF"])
ax.set_xlabel("Allele Frequency")
ax.set_ylabel("No. of Varients")
plt.savefig("ex2.png")
plt.close(fig)