#QBB2022 -Week1- Homework Exercises

1.1 1Mbp*5=5Mbp/100bp=50,000 reads for 5x coverage
    1Mbp*15=15Mbp/100bp=150,000 reads for 5x coverage
	
1.2 See code and histogram submitted

1.3 6941 nucleotides with no reads

1.4 3 nucleotides with no reads. The poisson function expects 0.306 reads for 0 which is lower that the count recorded by an order of magnitude. That said you cannot have a fractional number of reads so being in the low numbers makes sense.

2.1 samtools faidx contigs.fasta 
    less -S contigs.fasta.fai
   4 contigs produced

2.2 105830+47860+41351+39426=234,467 base pairs covered. Found by looking at file from above.
 
2.3 longest contig is 105,830 base pairs. Found by looking at file from above.

2.4 By looking at the sizes and some quick mental math N50 is 47,860.

3.1 After downgrading the Mummer version to make it work
	dnadiff ref.fa scaffolds.fasta
	less -S out.report
	Average Identity=99.98
	
3.2 nucmer ref.fa scaffolds.fasta
    show-coords out.delta
207,007 base pairs

3.3 1 insertion

4.1 it is from position 26,788 to position 27,497

4.2 using info from above  27497-26788=709 base pair insertion

4.3 samtools faidx scaffolds.fasta NODE_1_length_234497_cov_20.506978:26788-27497
ATACAATGCGTATTGTAGTATGGCCTTACGGGAGGGCAGACGGCAAAGAGTGATCACGTT
CTATCGGATGCAAGGCACCGCTTTATCCATTAGCCTCTTATTGGAGGAGGGCATGGCATT
CATACCCAATGGCTCAATTCTTTTACTACAACATTGATAACTTATCCAAGTACTCTACGA
CCAACCTGCAGAACGGCCCACCGGCCTAACGGCATACCTCACAACTACCCTGCTAAGGCG
AGCACTCCAGCCAAGCAAGACCACATCCACCCAAGCCCACCTCATCGCCTCAGCCAATAG
CGCTCAGACAAAAGGAACTTATTATTAACTGAAACGCTGTACTGCGGTAAGTCCTCAACG
CCGACCAAACGAAACCAGCAGCGTAGTCCTATCGGACTCGCTTGCACACATAACACATGC
TTGTAGTCTTGCACGACCCCAGGCGGACATGAGTTTCTGCTGGGCGGCGAGGAGTCGAAG
CTGCGGGCATTCCTTTCCGAAAACATGAATTACTGCGGGTATGTCCGACCTCAAACATTC
GTACCTGAGCATATTGCTCAAGTGAGCCAGTCGGCAATTCATATCCGAAAACATGACTGT
CTTGCATAAGGCCTCTCTTACGAGCTGAGTGCACGAACCACGGAACAGCTTAGTCACTTA
GAAGAGTACTCTATTCGGGACTTGAAGTACGCGTGCAATCGGGAACTAGT

4.4 python dna-decode.py --decode --input insertion.fasta
The decoded message :  Congratulations to the 2022 CMDB @ JHU class!  Keep on looking for little green aliens..
