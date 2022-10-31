#!/usr/bin/env python

import sys

import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def remove_dd_bg(mat):
     N = mat.shape[0]
     mat2 = numpy.copy(mat)
     for i in range(N):
         bg = numpy.mean(mat[numpy.arange(i, N), numpy.arange(N - i)])
         mat2[numpy.arange(i, N), numpy.arange(N - i)] -= bg
         if i > 0:
             mat2[numpy.arange(N - i), numpy.arange(i, N)] -= bg
     return mat2


def smooth_matrix(mat):
    N = mat.shape[0]
    invalid = numpy.where(mat[1:-1, 1:-1] == 0)
    nmat = numpy.zeros((N - 2, N - 2), float)
    for i in range(3):
        for j in range(3):
            nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
    nmat /= 9
    nmat[invalid] = 0
    return nmat
    
    
in1_fname, in2_fname, bin_fname, out_fname = sys.argv[1:5]
data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
    ('F1', int), ('F2', int), ('score', float)]))
data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([
    ('F1', int), ('F2', int), ('score', float)]))
frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
    ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

chrom = b'chr15'
start = 11170245
end = 12070245
start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                     (frags['start'] <= start) &
                                     (frags['end'] > start))[0][0]]
end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                   (frags['start'] <= end) &
                                   (frags['end'] > end))[0][0]] + 1
fil_data1=[]
fil_data2=[]
for line in data1:
    if line['F1']<start_bin:
        fil_data1.append(False)
    elif line['F2']>end_bin:
        fil_data1.append(False)
    else:
        fil_data1.append(True)
for line in data2:
    if line['F1']<start_bin:
        fil_data2.append(False)
    elif line['F2']>end_bin:
        fil_data2.append(False)
    else:
        fil_data2.append(True)

data1=data1[fil_data1]  
data2=data2[fil_data2]    

log_trans_1 = numpy.log(data1['score'])
min_val_1=min(log_trans_1)
data1['score']=log_trans_1-min_val_1
log_trans_2 = numpy.log(data2['score'])
min_val_2=min(log_trans_2)
data2['score']=log_trans_2-min_val_2

mat1=numpy.zeros((end_bin-start_bin,end_bin-start_bin))
mat2=numpy.zeros((end_bin-start_bin,end_bin-start_bin))
for i in range(len(data1['score'])):
    score=data1['score'][i]
    xcoord=data1['F1'][i]-start_bin-1
    ycoord=data1['F2'][i]-start_bin-1
    mat1[xcoord,ycoord]=score
    mat1[ycoord,xcoord]=score
for j in range(len(data2)):
    mcore=data2['score'][i]
    xcoord=data2['F1'][i]-start_bin-1
    ycoord=data2['F2'][i]-start_bin-1
    mat2[xcoord,ycoord]=score
    mat2[ycoord,xcoord]=score

mat1_smooth=smooth_matrix(mat1)
mat2_smooth=smooth_matrix(mat2)
mat1_rm_dd=remove_dd_bg(mat1_smooth)
mat2_rm_dd=remove_dd_bg(mat2_smooth)
difference_mat=mat2_rm_dd-mat1_rm_dd

fig,ax = plt.subplots(ncols=3)
ax[0].imshow(mat1, cmap='magma')
ax[0].set_title("ddCTCF")
ax[1].imshow(mat2, cmap='magma')
ax[1].set_title("dCTCF")
ax[2].imshow(difference_mat, cmap='seismic', norm=colors.CenteredNorm())
ax[2].set_title("Diference")
plt.tight_layout()
fig.savefig(out_fname)
plt.close(fig)
