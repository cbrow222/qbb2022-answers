#QBB2022-Week14 homework submission

#Step 1B
python make_krona_compatible.py metagenomics_data/step0_givendata/KRAKEN/SRR492183.kraken SRR492183
python make_krona_compatible.py metagenomics_data/step0_givendata/KRAKEN/SRR492186.kraken SRR492186
python make_krona_compatible.py metagenomics_data/step0_givendata/KRAKEN/SRR492188.kraken SRR492188
python make_krona_compatible.py metagenomics_data/step0_givendata/KRAKEN/SRR492189.kraken SRR492189
python make_krona_compatible.py metagenomics_data/step0_givendata/KRAKEN/SRR492190.kraken SRR492190
python make_krona_compatible.py metagenomics_data/step0_givendata/KRAKEN/SRR492193.kraken SRR492193
python make_krona_compatible.py metagenomics_data/step0_givendata/KRAKEN/SRR492194.kraken SRR492194
python make_krona_compatible.py metagenomics_data/step0_givendata/KRAKEN/SRR492197.kraken SRR492197

#Step 1C
ktImportText -o SRR492183.krona.html -q SRR492183_krona.txt 
ktImportText -o SRR492186.krona.html -q SRR492186_krona.txt 
ktImportText -o SRR492188.krona.html -q SRR492188_krona.txt 
ktImportText -o SRR492189.krona.html -q SRR492189_krona.txt 
ktImportText -o SRR492190.krona.html -q SRR492190_krona.txt 
ktImportText -o SRR492193.krona.html -q SRR492193_krona.txt 
ktImportText -o SRR492194.krona.html -q SRR492194_krona.txt 
ktImportText -o SRR492197.krona.html -q SRR492197_krona.txt

1:Initially there is a fair bit of Staphylococcus and Cutibacterium. The next day these groups both have gone down significantly. Then the Staphylococcus begin coming back and at the end Cutibacterium come up again.

#Step 2
2: We could do an alignment of reads to bacterial genomes and then group the contigs by this.

#Step2a
bwa index metagenomics_data/step0_givendata/assembly.fasta 

#Step2b
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata//READS/SRR492183_1.fastq metagenomics_data/step0_givendata/READS/SRR492183_2.fastq >SRR492183.sam
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata//READS/SRR492186_1.fastq metagenomics_data/step0_givendata/READS/SRR492186_2.fastq >SRR492186.sam
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata//READS/SRR492188_1.fastq metagenomics_data/step0_givendata/READS/SRR492188_2.fastq >SRR492188.sam
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata//READS/SRR492189_1.fastq metagenomics_data/step0_givendata/READS/SRR492189_2.fastq >SRR492189.sam
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata//READS/SRR492190_1.fastq metagenomics_data/step0_givendata/READS/SRR492190_2.fastq >SRR492190.sam
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata//READS/SRR492193_1.fastq metagenomics_data/step0_givendata/READS/SRR492193_2.fastq >SRR492193.sam
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata//READS/SRR492194_1.fastq metagenomics_data/step0_givendata/READS/SRR492194_2.fastq >SRR492194.sam
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata//READS/SRR492197_1.fastq metagenomics_data/step0_givendata/READS/SRR492197_2.fastq >SRR492197.sam

samtools sort -o SRR492183.bam SRR492183.sam
samtools sort -o SRR492186.bam SRR492186.sam
samtools sort -o SRR492188.bam SRR492188.sam
samtools sort -o SRR492189.bam SRR492189.sam
samtools sort -o SRR492190.bam SRR492190.sam
samtools sort -o SRR492193.bam SRR492193.sam
samtools sort -o SRR492194.bam SRR492194.sam
samtools sort -o SRR492197.bam SRR492197.sam

#Step 2D
jgi_summarize_bam_contig_depths --outputDepth depth.txt *.bam
metabat2 -i metagenomics_data/step0_givendata/assembly.fasta -a depth.txt -o bins_dir/bin

3a:I got 6 bins.
3b code
grep ">" bins_dir/bin.1.fa | wc -l
55 lines
grep ">" bins_dir/bin.2.fa | wc -l
78 lines
grep ">" bins_dir/bin.3.fa | wc -l
8 lines
grep ">" bins_dir/bin.4.fa | wc -l
37 lines
grep ">" bins_dir/bin.5.fa | wc -l
13 lines
grep ">" bins_dir/bin.6.fa | wc -l
6 lines

197 lines total
Percentages:
Bin 1: 28%
Bin 2: 40%
Bin 3: 4%
Bin 4: 19%
Bin 5: 7%
Bin 6: 3%

3c: The bin sizes seem weird because they are so inconsistant. 

3d: I would compare the length of the reads in the bins with the length of prokaryotic genomes and also blast the reads against prokaryotic genomes to see how many things they match up with and if the reads within a bin have consistant genome choices.

#Step 3

Predictions:
Bin 1: S t a p h y l o c o c c u s   a u r e u s
Bin 2: S t a p h y l o c o c c u s   e p i d e r m i d i s
Bin 3: A n a e r o c o c c u s   p r e v o t i i -This seemed mixed.
Bin 4: S t a p h y l o c o c c u s   h a e m o l y t i c u s
Bin 5: C u t i b a c t e r i u m   a v i d u m
Bin 6: E n t e r o c o c c u s   f a e c a l i s

4B: A better way would be to make the bins and then sort through the bins to find ones that have multiple strains identified and then look closer into that bin.