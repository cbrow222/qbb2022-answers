#!/usr/bin/env python

import numpy
import matplotlib.pyplot as plt

data=numpy.loadtxt("matrix/dCTCF_full.40000.matrix", dtype=numpy.dtype([
    ('F1', int), ('F2', int), ('score', float)]))
frags = numpy.loadtxt("matrix/40000_bins.bed", dtype=numpy.dtype([
    ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))
    
chrom=b'chr15'
start=10400000
end=13400000
start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                     (frags['start'] <= start) &
                                     (frags['end'] > start))[0][0]]
end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                   (frags['start'] <= end) &
                                   (frags['end'] > end))[0][0]] + 1

fil_data=[]
for line in data:
    if line['F1']<start_bin:
        fil_data.append(False)
    elif line['F2']>end_bin:
        fil_data.append(False)
    else:
        fil_data.append(True)

data=data[fil_data]

log_trans = numpy.log(data['score'])
min_val=min(log_trans)
data['score']=log_trans-min_val

mat=numpy.zeros((end_bin-start_bin,end_bin-start_bin))

for i in range(len(data['score'])):
    score=data['score'][i]
    xcoord=data['F1'][i]-start_bin-1
    ycoord=data['F2'][i]-start_bin-1
    mat[xcoord,ycoord]=score
    mat[ycoord,xcoord]=score

    
bin_range=range(5,(end_bin-start_bin-5))
insulation_score=[]
for i in bin_range:
    upstream_mean=numpy.mean(mat[(i - 5):i, i:(i + 5)])
    downstream_mean=numpy.mean(mat[i:(i+5),(i-5):i])
    insulation=(upstream_mean+downstream_mean)/2
    insulation_score.append(insulation)
    
fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
ax[0].axis('off')
ax[0].imshow(mat,cmap='magma')
plt.margins(x=0)
ax[1].plot(bin_range, insulation_score)
plt.subplots_adjust(left=0.15,
                bottom=0.1,
                right=1.0,
                top=1.0,
                wspace=0.4,
                hspace=0.0)
plt.savefig("insulation_plot.png")
plt.close()