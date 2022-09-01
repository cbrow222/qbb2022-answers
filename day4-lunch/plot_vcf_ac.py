#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )

vcf_name=sys.argv[1].split(".")
plot_name=f"{vcf_name[0]} SNP AC Values"
fig, ax = plt.subplots()
ax.hist( ac, density=True )
ax.set_xlabel("Allele Count")
ax.set_ylabel("Number of SNPs")
ax.set_title(plot_name)
plt.yscale('log')
plt.ylim([10**(-6),2*10**(-3)])
fig.savefig( vcf + ".png" )

fs.close()

