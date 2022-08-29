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
c. I would pull out each gene from the genes list and then pull out the number of exons in the range of that gene. I would then sort that list of numbers of exons per gene and then find the middle number. Or ask bash to do that if there is a command for that.

3.  