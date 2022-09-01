#!/usr/bin/env python

import numpy
from scipy.stats import binomtest
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.multitest import multipletests
import seaborn as sns

def simulate_coin_toss(n_tosses, prob_heads = 0.5, seed=None):
    '''
    Simulates a coin toss (fair or unfair depending on prob_heads)
    Input: n_tosses, an integer, number of coin tosses to simulate
           prob_heads, a float, the probability the coin toss will return heads; default is 0.5, meaning a fair coin
           seed, an integer, the random seed that will be used in the simulation; default is None
    Output: results_arr, an array of 1's and 0's with 1's representing heads and 0's representing tails
    Resources: https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    '''
    if seed is not None:
        numpy.random.seed(seed)
    results_arr = numpy.random.choice([0,1], size=n_tosses, p = [1-prob_heads, prob_heads])
    return (results_arr)

def perform_hypothesis_test(n_heads, n_tosses):
    '''
    Performs a two-sided binomial test
    Input: n_heads, an integer, number of coin tosses that resulted in heads/success
           n_tosses, an integer, total number of coin tosses/trials
    Output: pval, a float reporting the final pvalue from the binomial test
    Resources: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html#scipy.stats.binomtest
    '''
    binom_result = binomtest(n_heads, n_tosses)
    pval = binom_result.pvalue
    return(pval)

def correct_pvalues(pvals):
    '''
    Will apply the bonferroni multiple hypothesis testing correction method to input pvalues
    Input: pvals, an array-like object containing uncorrected pvalues
    Output: corrected_pvalues[1], an array containing corrected pvalues
    Resources: https://www.statsmodels.org/dev/generated/statsmodels.stats.multitest.multipletests.html
    '''
    corrected_pvalues = multipletests(pvals, method='bonferroni')
    return(corrected_pvalues[1])

def interpret_pvalues(pvals):
    '''
    Will interpret or convert pvalues from floats to booleans (Trues or Falses) reporting whether or not you reject the null hypothesis
    True -- reject null Hypothesis
    False -- fail to reject null hypothesis
    Input: pvals, an array-like object containing pvalues (floats)
    Output: interpreted, an array containing booleans
    '''
    interpreted = numpy.array(pvals) < 0.05
    return (interpreted)

def compute_power(n_rejected_correctly, n_tests):
    '''
    Will compute the power, defined as the number of correctly rejected null hypothesis divided by the total number of tests (AKA the True Positive Rate or the probability of detecting something if it's there)
    Input: n_rejected_correctly, an integer, the total number of tests in which the null hypothesis was correctly rejected
           n_tests, an integer, the total number of hypothesis tests which were performed
    output: power, a float, the power
    '''
    power = n_rejected_correctly / n_tests
    return(power)

def run_experiment(prob_heads, n_toss, n_iters = 100, seed = 389, correct_the_pvalues = False):
    '''
    Input: prob_heads, a float, the probability of a simulated coin toss returning heads
           n_toss, an integer, the number of coin tosses to simulate
           n_iters, an integer, the number of iterations for each simulation. default is 100
           seed, an integer, the random seed that you will set for the whole simulation experiment. default is 389
           correct_the_pvalues, a boolean, whether or not to perform multiple hypothesis testing correction
    Output: power, a float, the power of the experiment
    '''
    numpy.random.seed(seed)
    
    powers=numpy.zeros((len(prob_heads),len(n_toss)))
    for i, toss in enumerate(n_toss):
        for j, prob in enumerate(prob_heads):
            pvals=[]
            for k in range(n_iters):
                results_arr = simulate_coin_toss(toss, prob_heads = prob)
                n_success = numpy.sum(results_arr)
                pvals.append(perform_hypothesis_test(n_success, toss))
            if correct_the_pvalues:
                pvals = correct_pvalues(pvals)
            pvals_translated_to_bools = interpret_pvalues(pvals)
            powers[j,i] = compute_power(numpy.sum(pvals_translated_to_bools), n_iters)
    return(powers)
probs=numpy.around(numpy.arange(0.55,1.05,0.05),decimals=2)[::-1]
tosses=numpy.array([10,50,100,250,500,1000])
powers1=run_experiment(probs, tosses)
powers2=run_experiment(probs, tosses, correct_the_pvalues=True)

fig,ax=plt.subplots(ncols=2)
sns.heatmap(powers1, ax=ax[0],vmin=0, vmax=1, cmap="viridis", xticklabels=tosses, yticklabels=probs, cbar=False)
sns.heatmap(powers2, ax=ax[1],vmin=0, vmax=1, cmap="viridis", xticklabels=tosses, yticklabels=probs)
ax[0].set_ylabel("Probability of a Head")
ax[0].set_xlabel("Number of Tosses")
ax[1].set_ylabel("Probability of a Head")
ax[1].set_xlabel("Number of Tosses")
ax[0].set_title("No P-value Correction")
ax[1].set_title("P-value Correction")
plt.tight_layout()
fig.savefig("exC.png")
plt.close(fig)