#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def allele_freq_to_fix(allele_freq, pop_size):
    allele_freq_gen=[allele_freq]
    while allele_freq>0 and allele_freq<1:
        n=pop_size*2
        p=allele_freq
        allele_freq=np.random.binomial(n, p)/n
        allele_freq_gen.append(allele_freq)
    return(allele_freq_gen)
    
def plot_allele_freq(allele_freq_gen, allele_freq, pop_size):
    x=range(0, len(allele_freq_gen))
    fig, ax = plt.subplots()
    ax.plot(x, allele_freq_gen)
    ax.set_xlabel("Generation")
    ax.set_ylabel("Allele Frequency")
    ax.set_title(f"Starting allele frequency={allele_freq} and population size={pop_size}")
    fig.savefig(f"Allele_freq_overtime{allele_freq}_{pop_size}.png")
    plt.close(fig)

#Question 2    
# allele_freq_gen=allele_freq_to_fix(0.7, 100)
# plot_allele_freq(allele_freq_gen, 0.7, 100)
#
# #Question 3
# generations=[]
# for i in range(0,10000):
#     allele_freq_gen=allele_freq_to_fix(0.5,100)
#     generations.append(len(allele_freq_gen))
#
# fig,ax = plt.subplots()
# ax.hist(generations)
# ax.set_xlabel("Number of Generations")
# ax.set_ylabel("Number of Trials")
# fig.savefig("histogram_of_generations_to_fixation.png")
# plt.close(fig)
#
# #Question 4
# population_sizes=[100,1000,10000,100000,1000000,10000000]
# generations=[]
# for pop_size in population_sizes:
#     allele_freq_gen=allele_freq_to_fix(0.5, pop_size)
#     generations.append(len(allele_freq_gen))
#
# fig,ax = plt.subplots()
# ax.plot(population_sizes, generations)
# ax.set_xlabel("Population Size (log-scale)")
# ax.set_ylabel("Generations to Fixation")
# ax.set_xscale("log")
# fig.savefig("Generations_to_fixation_by_population.png")
# plt.close(fig)

#Question 5
allele_frequencies=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
generations=[]
for j,allele_freq in enumerate(allele_frequencies):
    gen=[]
    for i in range(0,100):
        allele_freq_gen=allele_freq_to_fix(allele_freq, 100)
        gen.append(len(allele_freq_gen))
    generations.append(gen)
    
fig,ax=plt.subplots()
ax.boxplot(generations, vert=True, labels=allele_frequencies)
ax.set_xlabel("Allele Frequencies")
ax.set_ylabel("Generations to Fixation")
fig.savefig("Generations_to_fixation_by_allele_freq.png")
plt.close(fig)
