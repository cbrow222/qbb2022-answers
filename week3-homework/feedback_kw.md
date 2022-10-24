# Week 3 Variant Calling -- Feedback

0 + 1 + 1 + 0.75 + 1 + 1 + 1 + 1 + 1 + 1 = 8.75 points out of 10 possible points

1. Index genome

  * what code did you use? --> +0

2. align reads

  * --> +1
  * I would recommend listing all the samples if you're going to say something like "Repeat this line for each sample". Alternatively, you could employ a `for` loop in bash:
  ```
  for ID in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63; do
  	bwa mem -t 4 -R "@RG\tID:${ID}\tSM:${ID}"  sacCer3.fa ${ID}.fastq > aln_${ID}.sam
    samtools sort -O bam aln_${ID}.sam > aln_${ID}.bam
    samtools index -b aln_${ID}.bam aln_${ID}.bam.bai
  done
  ```

3. sort bam files and index sorted bam files (0.5 points each)

  * --> +1

4. variant call with freebayes

  * want to use the `-p` argument to specify the ploidy of the yeast (1)
  * --> +0.75

5. filter variants

  * --> +1

6. decompose complex haplotypes

  * --> +1

7. variant effect prediction

  * --> +1

8. python plotting script

  * --> +1
  * fantastic way of getting the uniq effects and the corresponding counts for the bar plot!

9. 4 panel plot (0.25 points each panel)

  * --> +1

10. 1000 line vcf

  * --> +1
