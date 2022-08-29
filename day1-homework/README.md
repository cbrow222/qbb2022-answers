#QBB Day 1 Homework Exercise Solutions
1.Error message: illegal field $(), name "nuc"
Fix: The variable "nuc" was not defined in the awk statement so it needed to be defined with the flag -v at the beginning of the awk statement.
Output:
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
This makes sense because the most likely replacement for a purine is the other purine and the most common replacement for a pyridine is a pyridine.

2. Promotors appear to be defined in classes 1 (Active Transcription Start Sites), 2 (regions flanking the sites in class 1), 10 (Bivalent/Poised Transcription Start Sites), 11 (regions flanking sites in class 10). This is not terribly clear to the reader and a better definition in the write-up would be nice. The promotors are not as easy to identify as you would like.
Reasoning: I want to identify the relavant sections using awk then intersect the two files with SNPs as a and the promotors as b. Then use awk to determine the replacements to cytosine.
Code: #Usage C_SNP_replacements_promoters.sh vcf_file bed_file

grep -Ew '1|2|10|11' $2 > promoters.bed
bedtools intersect -a $1 -b promoters.bed | awk '/^#/{next} {if ($4 == "C") {print $5}}' | sort | uniq -c
  12 A
  11 G
  39 T
The most common replacement in these areas is T, which is the same as in the whole dataset. My hypothesis from above continues to be valid.

3. Line 5 Removes header, converts the vcf into bed format
Line 6 sorts genes by chromosome and then start site
Line 7 identifies genes closest to the varients
Error 1: unable to open file or unable to determine types for file variants.bed
Fix 1: The file made by awk was not tab delineated. Adding that specification fixes the problem.
Error 2: Sorted input specified, but the file variants.bed has the following out of order record
Fix 2: Sort the variants.bed file
There are 10293 variants and 200 unique genes.
wc -l closest.bed #find number of varients
cut -f 7 closest.bed | sort | uniq | wc -l #number of genes
This averages out to 51.465 varients per gene.

4. Line 7 finds H3K27ac marked genes
Line9 finds H3K9me3 marked genes
Line 11 finds genes with H3K27ac and no H3K9me3 markings
Syntax Errors: the files weren't in our directory, we fixed this before running
Logic Error: the file names in grep are switched
Output: CRYAA

