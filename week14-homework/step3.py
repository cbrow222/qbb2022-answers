#!/usr/bin/env python

import numpy as np

bin1=np.genfromtxt("bins_dir/bin.1.fa", dtype = None, encoding=None)
bin2=np.genfromtxt("bins_dir/bin.2.fa", dtype = None, encoding=None)
bin3=np.genfromtxt("bins_dir/bin.3.fa", dtype = None, encoding=None)
bin4=np.genfromtxt("bins_dir/bin.4.fa", dtype = None, encoding=None)
bin5=np.genfromtxt("bins_dir/bin.5.fa", dtype = None, encoding=None)
bin6=np.genfromtxt("bins_dir/bin.6.fa", dtype = None, encoding=None)

assembly=open("metagenomics_data/step0_givendata/KRAKEN/assembly.kraken", 'r')

bins=[bin1,bin2,bin3,bin4,bin5,bin6]

def kraken_parser(assembly):
    genus_dict= dict()
    species_dict= dict()
    for line in assembly:
        fields=line.split()
        name = fields[0]
        taxonomy=' '.join(line[1:]).split(';')
        try:
            genus=taxonomy[8]
        except:
            genus='-'
        try:
            species=taxonomy[9]
        except:
            species='-'
        genus_dict[name]=genus
        species_dict[name]=species
    return genus_dict, species_dict
    
def count_ids(names, id_dict, idname=''):
    counts=dict()
    for name in names:
        category=id_dict[name]
        if category in counts:
            counts[category] += 1
        else:
            counts[category] = 1
    print('\tCategories identified in bin: {}'.format(counts))

genus_dict, species_dict = kraken_parser(assembly)

for i in bins:
    names = []
    for line in i:
        if line.startswith('>'):
            names.append(line.strip('>\n'))
    count_ids(names, genus_dict, 'genus')
    count_ids(names, species_dict, 'species')