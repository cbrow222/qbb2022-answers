#QBB2022 -  Day 1 - Lunch Exercises Submission
1. I'm excited to  learn how to interact with Unix and to get better with Python.
2. 
a. (base) [~/qbb2022-answers/day1-lunch $]cp ~/data/bed_files/genes.chr21.bed .
   (base) [~/qbb2022-answers/day1-lunch $]cp ~/data/bed_files/exons.chr21.bed .
b. (base) [~/qbb2022-answers/day1-lunch $]wc -l genes.chr21.bed
     219 genes.chr21.bed
   (base) [~/qbb2022-answers/day1-lunch $]wc -l exons.chr21.bed 
     13653 exons.chr21.bed
 13653/219= 62.34 exons per gene on average
c. I would pull out each gene from the genes list and then pull out the number of exons in the range of that gene. (Find exons that fall between the region of a gene.) I would then sort that list of numbers of exons per gene and then find the middle number. Or ask bash to do that if there is a command for that. (This wouldn't work well in bash.)

3.
a. (base) [~/qbb2022-answers/day1-lunch $]cp ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed .
b.(base) [~/qbb2022-answers/day1-lunch $]sort -k 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | uniq -f 3 -c (Could us sort -nk4 instead to get in properly numeric order)
State 1: 305
State 2: 678
State 3: 79
State 4: 377
State 5: 808
State 6: 148
State 7: 1050
State 8: 156
State 9: 654
State 10: 17
State 11: 17
State 12: 30
State 13: 62
State 14: 228
State 15: 992
c. I'd start by sorting by state (sork -k 4). Then I would find the difference between the start and end sites for each line and make that length a separate column to work with. I would add the lengths for each example of a state together to get a total length of the state. Then I would take each of those state lengths and divide by the total length (all the states added together). Then I could compare the percentages. This would be easier to do using R.
4. 
a. (base) [~/qbb2022-answers/day1-lunch $]cp ~/data/metadata_and_txt_files/integrated_call_samples.panel .
b. (base) [~/qbb2022-answers/day1-lunch $]grep AFR integrated_call_samples.panel | sort -k 2 | cut -f 2 | uniq -c
 123 ACB
 112 ASW
 173 ESN
 180 GWD
 122 LWK
 128 MSL
 206 YRI
c. You could manually repeat naming out the different super populations in the grep and end up with 5 lines of code. You could also not grep and instead sort by the population (and super-population) and then cut out the population and super-population information and then use the uniq -c to pull out the unique populations tagged with where they are from and how many times they repeat.
5.
a.(base) [~/qbb2022-answers/day1-lunch $]cp ~/data/vcf_files/random_snippet.vcf . 
b.(base) [~/qbb2022-answers/day1-lunch $]cut -f -9,13 random_snippet.vcf > HG00100
c.(base) [~/qbb2022-answers/day1-lunch $]cut -f 10 HG00100 | sort | uniq -c
9514 0|0
 127 0|1
 178 1|0
 181 1|1
d. (base) [~/qbb2022-answers/day1-lunch $]grep AF=1 HG00100 | wc -l
      34
e. By manually counting: 6 times
f. I would cut out the correct column. Then I would cycle through the semi-colon separated list in each row to find the AFR value to print it out.