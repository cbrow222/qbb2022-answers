#QBB2022-Week8 Homework Submissions

Part 1:
medaka_variant -f hg38.fa -i methylation.bam -r chr11:1900000-2800000 -o chr11 -p chr11_phased.vcf.gz

medaka_variant -f hg38.fa -i methylation.bam -r chr14:100700000-100990000 -o chr14 -p chr14_phased.vcf.gz

medaka_variant -f hg38.fa -i methylation.bam -r chr15:23600000-25900000 -o chr15 -p chr15_phased.vcf.gz

medaka_variant -f hg38.fa -i methylation.bam -r chr20:58800000-58912000 -o chr20 -p chr20_phased.vcf.gz

Part 2:
whatshap haplotag -o chr11_haplotag.bam --reference hg38.fa --output-haplotag-list chr11_haplotypes.tsv chr11/round_0_hap_mixed_phased.vcf.gz chr11/methylation.bam

whatshap haplotag -o chr14_haplotag.bam --reference hg38.fa --output-haplotag-list chr14_haplotypes.tsv chr14/round_0_hap_mixed_phased.vcf.gz chr14/methylation.bam

whatshap haplotag -o chr15_haplotag.bam --reference hg38.fa --output-haplotag-list chr15_haplotypes.tsv chr15/round_0_hap_mixed_phased.vcf.gz chr15/methylation.bam

whatshap haplotag -o chr20_haplotag.bam --reference hg38.fa --output-haplotag-list chr20_haplotypes.tsv chr20/round_0_hap_mixed_phased.vcf.gz chr20/methylation.bam

Part 3:

whatshap split --output-h1 hap1_chr11.bam --output-h2 hap2_chr11.bam chr11/methylation.bam chr11_haplotypes.tsv

whatshap split --output-h1 hap1_chr14.bam --output-h2 hap2_chr14.bam chr14/methylation.bam chr14_haplotypes.tsv

whatshap split --output-h1 hap1_chr15.bam --output-h2 hap2_chr15.bam chr15/methylation.bam chr15_haplotypes.tsv

whatshap split --output-h1 hap1_chr20.bam --output-h2 hap2_chr20.bam chr20/methylation.bam chr20_haplotypes.tsv

Part 6:

No I do not expect that to be the case because the haplotypes are not linked between the regions. They are on different chromosomes and thus are not connected and the haplotypes are not part of the same thing.