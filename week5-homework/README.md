#QBB2022-Week5 Homework Solutions
PART1:
1: samtools view -b -e qual >=10 D2_Sox2_R1.bam
samtools view -b -e qual >=10 D2_Sox2_R2.bam

2:macs2 callpeak -B -n R1 -t D2_Sox2_R1.bam
macs2 callpeak -B -n R2 -t D2_Sox2_R2.bam

3: bedtools intersect -a R1_peaks.narrowPeak -b R2_peaks.narrowPeak > intersected.bed

4: Sox2 peaks: 2106
Klf4 peaks: 60
both: 52 peaks
% Klf4 peaks with Sox2: 86.7%

5:python scale_bdg.py D0_H3K27ac_treat.bdg D0_H3K27ac_scaled.bdg
python scale_bdg.py D2_H3K27ac_treat.bdg D2_H3K27ac_scaled.bdg
python scale_bdg.py D2_Klf4_treat.bdg D2_Klf4_scaled.bdg
python scale_bdg.py R1_treat_pileup.bdg D2_Sox2_scaled.bdg

awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D2_Sox2_scaled.bdg >  D2_Sox2_scaled_cropped.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D2_Klf4_scaled.bdg > D2_Klf4_scaled_cropped.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D2_H3K27ac_scaled.bdg > D2_H3K27ac_scaled_cropped.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D0_H3K27ac_scaled.bdg > D0_H3K27ac_scaled_cropped.bdg

PART2:
1-3: sort -k 5,5rn intersected.bed|head -300|awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' > 300_sorted_peaks.narrowPeak

4: samtools faidx mm10.fa -r 300_sorted_peaks.narrowPeak > peak_sequences.fa

5: meme-chip -maxw 7 peak_sequences.fa

Part3:
1:tomtom memechip_out/combined.meme /Users/cmdb/Downloads/motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme

2: open tomtom_out/tomtom.html

3: grep -e Klf4 -e Sox2 tomtom_out/tomtom.tsv > Klf4_Sox2_motif.tsv