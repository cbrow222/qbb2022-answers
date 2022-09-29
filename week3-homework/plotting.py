#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

vcf=open("annotated.vcf")

read_depth=[]
quality=[]
allele_frequency=[]
predicted_effect=[]
for line in vcf:
    if line.startswith("#"):
        continue
    line=line.split()
    for i in range(9,19):
        line[i]=line[i].split(":")
        read_depth.append(line[i][2])
        quality.append(line[i][1])
    line[7]=line[7].split(";")
    for entry in line[7]:
        tag=entry.split("=")[0]
        if tag=="AF":
            if len(entry.split("=")[1].split(","))==1:
                allele_frequency.append(float(entry.split("=")[1]))
            else:
                allele_frequency.append(float(entry.split("=")[1].split(",")[0]))
        elif tag=="ANN":
            predicted_effect.append(entry.split("=")[1].split("|")[2])
        
uniq_effect,effect_counts=np.unique(predicted_effect, return_counts=True)

fig,ax = plt.subplots(nrows=2, ncols=2)
ax[0,0].hist(read_depth, bins=50)
ax[0,0].set_xlabel("Read Depth")
ax[0,0].set_ylabel("No. of Samples")
ax[0,0].set_xlim(0,40)
ax[0,0].set_xticks([0,5,10,15,20,25,30,35,40])
ax[0,0].set_xticklabels([0,5,10,15,20,25,30,35,40])
ax[0,1].hist(quality)
ax[0,1].set_xlabel("Quality (Phred-scaled)(*10^4)")
ax[0,1].set_ylabel("No. of Variants")
ax[0,1].set_xticks([0,20000,40000,60000,80000,100000,120000,140000,160000,180000,200000,220000,240000])
ax[0,1].set_xticklabels([0,2,4,6,8,10,12,14,16,18,20,22,24])
ax[1,0].hist(allele_frequency)
ax[1,0].set_xlabel("Allele Frequency")
ax[1,0].set_ylabel("No. of Variants")
ax[1,1].bar(uniq_effect,effect_counts)
ax[1,1].set_xlabel("Predicted Effect")
ax[1,1].set_ylabel("No. of Variants")
plt.xticks(rotation = 90)
plt.tight_layout()
fig.savefig("step8.png")
plt.close()