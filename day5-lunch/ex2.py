#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats

fs=np.genfromtxt("data.txt", delimiter=' ', dtype=None, encoding=None, names=["Proband_ID", "mut_from_father", "mut_from_mother", "father_age", "mother_age"])

fig, ax = plt.subplots()
ax.scatter(fs["mother_age"],fs["mut_from_mother"])
ax.set_ylabel("Mutations from Mother")
ax.set_xlabel("Mother's Age")
fig.savefig("ex2_a.png")
plt.close(fig)

fig, ax = plt.subplots()
ax.scatter(fs["father_age"],fs["mut_from_father"])
ax.set_ylabel("Mutations from Father")
ax.set_xlabel("Father's Age")
fig.savefig("ex2_b.png")
plt.close(fig)

mother_model = smf.ols(formula = "mother_age ~1 + mut_from_mother", data = fs).fit()
father_model = smf.ols(formula = "father_age ~1 + mut_from_father", data = fs).fit()
#print(father_model.summary())

fig, ax = plt.subplots()
ax.hist(fs["mut_from_father"], alpha=0.5, label="Mutations from Father")
ax.hist(fs["mut_from_mother"], alpha=0.5, label="Mutations from Mother")
ax.set_xlabel("Mutations per Proband")
ax.set_ylabel("Number of Probands")
ax.legend()
fig.savefig("ex2_c.png")
plt.close(fig)

print(stats.ttest_ind(fs["mother_age"], fs["father_age"]))

new_data = fs[0]
new_data.fill(0)
new_data["father_age"]=50.5
print(father_model.predict(new_data))