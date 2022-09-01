#QBB2022 - Day 4- Lunch Exercises Solutions

Exercise 1:
--- Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp

Open both the plot that was created and the plot from the cache/ directory and then look at the two plots to compare.

Gene_type
1. miRNA-MicroRNAs are not protein coding but they are very important for controling gene expression which makes them interesting
2. lncRNA-Long noncoding RNAs are also not protein coding. They also are important for controlling cellular processes which makes them interesting.
3. transcribed_unprocessed_pseudogene- I don't know much about pseudogenes which makes them interesting to me. That this category is unprocessed distiguishes them from the category that gets plotted, but adds another layer of mystery to them to me and makes them interesting.

Exercise 2:
In all the graphs, most SNPs appear to a low allele count, with the number of SNPs decreasing as the allele count increases.

Exercise 3:-documentation
Synopsis
	bxlab/cmdb-plot-vcfs takes a vcf and a gtf file and catagorizes the SNPs into gene types and then plots the SNPs by gene type in a histogram based on allele count.
Usage:
	bash do_all.sh <vcf_file.vcf> <gtf_file.gtf>
Dependencies:
	matplotlib.pyplot bedtools
Description:
	1. Creates .bed files describing the locations of features of interest in the .gtf file
		-run bash subset_regions.sh
		-grep to pull out the features of interest
		-uses awk to print the relavent data from those lines into a .bed file
	2.Determines how many base pairs each region covers
		 -uses bedtools to read through the bed file
		 -adds up the starting location and subtracts the ending location
	3.Finds the SNPs in each region and creates a .vcf file
		-use bedtools to intersect the bed file with the provided .vcf file to identify SNPs in the region
		-saves the resulting file
	3. Plots the allele counts for the SNPs in each .vcf file and saves in a .png file
		-run plot_vcf_ac.py
		-looks through each line to find the allele count for the SNP and save it in a list
		-uses matplotlib.pyplot to plot allele counts as a histogram with a log scale
Output:
1.annotation.gtf
*** Creating .bed files for features of interest
--- Creating protein_coding.chr21.bed
--- Creating processed_pseudogene.chr21.bed
--- Creating lncRNA.chr21.bed
--- Creating exons.chr21.bed
*** Subsetting .vcf for each feature
--- Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting lncRNA.chr21.bed.vcf
    + Covering 8663528 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp
*** Plotting AC for each .vcf
--- Plotting AC for exons.chr21.bed.vcf
--- Plotting AC for lncRNA.chr21.bed.vcf
--- Plotting AC for processed_pseudogene.chr21.bed.vcf
--- Plotting AC for protein_coding.chr21.bed.vcf
--- Plotting AC for random_snippet.vcf

Sample plots found in this directory