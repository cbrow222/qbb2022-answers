#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from bdg_loader import load_data

D0ac=load_data("D0_H3K27ac_scaled_cropped.bdg")
D2ac=load_data("D2_H3K27ac_scaled_cropped.bdg")
Klf4=load_data("D2_Klf4_scaled_cropped.bdg")
Sox2=load_data("D2_Sox2_scaled_cropped.bdg")

fig, ax=plt.subplots(nrows=4)
ax[0].plot(D0ac["X"],D0ac["Y"])
ax[1].plot(D2ac["X"],D2ac["Y"])
ax[2].plot(Klf4["X"],Klf4["Y"])
ax[3].plot(Sox2["X"],Sox2["Y"])
ax[0].set_ylabel("Day 0 H3K27ac")
ax[1].set_ylabel("Day 2 H3K27ac")
ax[2].set_ylabel("Klf4")
ax[3].set_ylabel("Sox2")
ax[3].set_xlabel("Genomic Location")
plt.tight_layout()
fig.savefig("step5.png")
plt.close(fig)