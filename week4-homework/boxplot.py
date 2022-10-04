#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

SNPoi="rs7257475"
rowoi=240916

vcfall=np.genfromtxt("gwas_data/genotypes.vcf",dtype=None, encoding=None)
phenodata=np.genfromtxt("gwas_data/GS451_IC50.txt",dtype=[int,int,float], encoding=None, names = True)
lineoi=vcfall[240916]

Ref=lineoi[3]
Alt=lineoi[4] 
count=0
homorefphen=[]
homoaltphen=[]
hetphen=[]   
for i in range(9,len(lineoi)):
    if np.isnan(phenodata[count][2]):
        count+=1
        continue
    elif lineoi[i]=="0/0":
        homorefphen.append(phenodata[count][2])
    elif lineoi[i]=="1/1":
        homoaltphen.append(phenodata[count][2])
    elif lineoi[i]=="0/1" or lineoi[i]=="1/0":
        hetphen.append(phenodata[count][2])
    count+=1

labels=[f"{Ref}/{Ref}", f"{Ref}/{Alt}", f"{Alt}/{Alt}"]
plots=[homorefphen, hetphen, homoaltphen]
fig,ax = plt.subplots()
ax.boxplot(plots, vert=True, labels=labels)
ax.set_xlabel("Genotype")
ax.set_ylabel("IC50")
plt.savefig("boxplot.png")
plt.close(fig)