#!/usr/bin/env python
#Usage: python aligner.py <fasta_file> <scoring_matrix> gap_penalty <file_for_saving>

from fasta import readFASTA
import sys
import numpy as np

input_sequences = readFASTA(open(sys.argv[1]))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

score_names=[]
sub_matrix=open(sys.argv[2])
score_matrix=[]
for i, line in enumerate(sub_matrix):
    if i>=1:
        score_matrix.append(line.strip('\n').split()[1:])
    elif i==0:
        score_names=(line.strip('\n').split())

gap_penalty=float(sys.argv[3])

#initialize matricies
F_matrix=np.zeros((len(sequence1)+1,len(sequence2)+1))
traceback_matrix=np.empty((len(sequence1)+1,len(sequence2)+1))
#fill in first row and column
for i in range(0,F_matrix.shape[0]):
    F_matrix[i,0]=i*gap_penalty

for j in range(0,F_matrix.shape[1]):
    F_matrix[0,j]=j*gap_penalty
#fill in the rest
for i in range(1,F_matrix.shape[0]):
    for j in range(1,F_matrix.shape[1]):
        column=int(score_names.index(sequence1[i-1]))
        row=int(score_names.index(sequence2[j-1]))
        d=F_matrix[i-1,j-1]+float(score_matrix[row][column])
        h=F_matrix[i,j-1]+gap_penalty
        v=F_matrix[i-1,j]+gap_penalty
        F_matrix[i,j]=max(d,h,v)
        if d>=h and d>=v:
            traceback_matrix[i,j]=1
        elif h>=v:
            traceback_matrix[i,j]=2
        else:
            traceback_matrix[i,j]=3

#Traceback
i=len(sequence1)
j=len(sequence2)
alignment_score=F_matrix[i,j]
seq1_align=[]
seq2_align=[]
gap_count_1=0
gap_count_2=0
while i>0 and j>0:
    if traceback_matrix[i,j]==1: #d
        seq1_align.append(sequence1[i-1])
        seq2_align.append(sequence2[j-1])
        i-=1
        j-=1
    elif traceback_matrix[i,j]==2: #h
        seq1_align.append("-")
        seq2_align.append(sequence2[j-1])
        j-=1
        gap_count_1+=1
    elif traceback_matrix[i,j]==3: #v
        seq1_align.append(sequence1[i-1])
        seq2_align.append("-")
        i-=1
        gap_count_2+=1

alignment=[seq1_id, ''.join(seq1_align),seq2_id, ''.join(seq2_align)]
output_file=open(sys.argv[4], "w")
for element in alignment:
    output_file. write(element+'\n')
output_file. close()
print(f"There are {gap_count_1} gaps in sequence 1")
print(f"There are {gap_count_2} gaps in sequence 2")
print(alignment_score)