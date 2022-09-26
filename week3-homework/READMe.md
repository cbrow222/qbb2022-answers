#QBB2022-Week 3-Homework Exercise solutions

Part 2:
Repeat this line for each sample:
bwa mem -R "@RG\tID:A01_63\tSM:A01_63" sacCer3.fa A01_63.fastq > aln_A01_63.sam

Part 3a:
samtools sort -O bam aln_A01_63.sam > aln_A01_63.bam

Part 3b:
samtools index -b aln_A01_63.bam aln_A01_63.bam.bai

Part 4:
freebayes -f sacCer3.fa -v var.vcf aln_A01_09.bam aln_A01_11.bam aln_A01_23.bam aln_A01_24.bam aln_A01_27.bam aln_A01_31.bam aln_A01_35.bam aln_A01_39.bam aln_A01_62.bam aln_A01_63.bam

Part 5:
vcffilter -f "QUAL > 20" var.vcf >results.vcf

Part 6:
vcfallelicprimitives -k -g results.vcf > decomposed.vcf

Part 7:
snpeff ann R64-1-1.99 decomposed.vcf > annotated.vcf