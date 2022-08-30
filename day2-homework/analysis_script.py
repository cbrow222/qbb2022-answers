#!/user/bin/env python3
import sys
from vcfParser import parse_vcf #import function

kgp="random_snippet.vcf" #load 1KGP file
dbSNP="dbSNP_snippet.vcf" #load dbSNP file

dbSNP_parsed=parse_vcf(dbSNP) #parse dbSNP file
kgp_parsed=parse_vcf(kgp) #parse 1KGP file

#position=0 #initialize position variable
#IDs=0 #initialize ID variable
pos_ID_dic={} #initialize dictionary
for i, line in enumerate(dbSNP_parsed): #loop through dbSNP
    if i>=1: #ignore header line
        position=line[1] #store position
        IDs=line[2] #store ID
        pos_ID_dic[position]=IDs#make dictionary entry
lines_no_ID=0 #initialize counter for lines without ID
for i, line in enumerate(kgp_parsed): #loop through lines in 1KPG
    if i>=1: #ignore header line
        keyoi=line[1] #identify key of interest
        if keyoi in pos_ID_dic: #if that key is in the dictionary
            kgp_parsed[i][2]=pos_ID_dic[keyoi] #replace ID with value
        else: #if not
            lines_no_ID += 1 #add to the no ID line count


print(f"There are {lines_no_ID} lines without IDs.") #print lines without IDs