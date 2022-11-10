#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import numpy.lib.recfunctions as rfn
import scipy
import statsmodels.formula.api as smf
import statsmodels.api as sm
import statsmodels.stats as sms

input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')

col_names = list(input_arr.dtype.names)
row_names = input_arr["t_name"]


fpkm_values=input_arr[col_names[1:]]
fpkm_values_2d = rfn.structured_to_unstructured(fpkm_values, dtype=float)

medians=np.median(fpkm_values_2d,axis=1)
roi=np.where(medians)
fpkm=fpkm_values_2d[roi]
row_names_kept=row_names[roi]
fpkm_transform=np.log2(fpkm+0.1)
fpkm_transform_transpose=fpkm_transform.T

# linkage_col=scipy.cluster.hierarchy.linkage(fpkm_transform, method="ward")
# leaves_col=scipy.cluster.hierarchy.leaves_list(linkage_col)
# linkage_row=scipy.cluster.hierarchy.linkage(fpkm_transform_transpose, method="ward")
# leaves_row=scipy.cluster.hierarchy.leaves_list(linkage_row)
#
# row_sorted=fpkm_transform[:,leaves_row]
# full_sorted=fpkm_transform[leaves_col,:]
# fig, ax = plt.subplots()
# ax.imshow(full_sorted, aspect='auto')
# ax.set_xlabel("Samples")
# ax.set_ylabel("Genes")
# plt.savefig("heatmap.png")
# plt.close(fig)
#
# fig= plt.figure(figsize=(25, 10))
# dn=scipy.cluster.hierarchy.dendrogram(linkage_row)
# fig.suptitle("Sample Relatedness")
# plt.savefig("dendrogram.png")
# plt.close(fig)

sexes=[]
stages=[]
for l in col_names[1:]:
    sexes.append(l.split('_')[0])
    stages.append(l.split('_')[1])

betas=[]
pvalues=[]    
for i in range(fpkm_transform.shape[0]):
    list_of_tuples=[]
    for j in range(len(col_names)-1):
        list_of_tuples.append((row_names_kept[i],fpkm_transform[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    model=smf.ols(formula="fpkm ~ stage", data=longdf).fit()
    pvalues.append(model.pvalues["stage"])
    betas.append(model.params["stage"])
    
fig,ax = plt.subplots()
sm.qqplot(np.array(pvalues), dist=scipy.stats.uniform, line='45')
plt.tight_layout()
plt.savefig("qqplot.png")
plt.close(fig)

multitest=sms.multitest.multipletests(pvalues,alpha=0.1, method="fdr_bh")
significant=row_names_kept[multitest[0]]
print(significant)

betas2=[]
pvalues2=[]    
for i in range(fpkm_transform.shape[0]):
    list_of_tuples=[]
    for j in range(len(col_names)-1):
        list_of_tuples.append((row_names_kept[i],fpkm_transform[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    model=smf.ols(formula="fpkm ~ stage+sex", data=longdf).fit()
    pvalues2.append(model.pvalues["stage"])
    betas2.append(model.params["stage"])

multitest2=sms.multitest.multipletests(pvalues,alpha=0.1, method="fdr_bh")
significant2=row_names_kept[multitest[0]]
print(significant2)

overlap = set(significant) & set(significant2)
percent_overlap=len(overlap)/len(significant)*100
print(percent_overlap)

pvalsig=[]
betasig=[]
pvalnotsig=[]
betanotsig=[]
for i,pval in enumerate(pvalues2):
    if pval<0.1:
        pvalsig.append(-np.log10(pval))
        betasig.append(betas2[i])
    else:
        pvalnotsig.append(-np.log10(pval))
        betanotsig.append(betas2[i])
        
fig,ax=plt.subplots()
ax.scatter(betasig, pvalsig)
ax.scatter(betanotsig, pvalnotsig)
ax.set_xlabel("Beta")
ax.set_ylabel("-log10(p)")
plt.savefig("volcano_plot.png")
plt.close(fig)
