from bed_parser import parse_bed
import sys
bed=parse_bed(sys.argv[1])

exon_number=[]
for i in range(len(bed)):
    exon_number.append(bed[i][9])
exon_number.sort()
median_index=int(len(exon_number)/2)
median=exon_number[median_index]
print(f"The median number of exons is {median}.")