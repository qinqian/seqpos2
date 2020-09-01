#!/bin/bash

#mysql --user=genome --host=genome-mysql.cse.ucsc.edu -A -e \
#        "select chrom, size from hg38.chromInfo" > hg38.genome

# human
# 1000bp windows
#bedtools makewindows -g hg38.genome -w 1000 | awk '{OFS="\t"; print $1,$2,$3,NR}'> hg38_window1kb.bed

# human 200bp windows for GC
#bedtools makewindows -g hg38.genome -w 200 | awk '{OFS="\t"; print $1,$2,$3,NR}'> hg38_window200bp.bed

# 100bp windows
#bedtools makewindows -g hg38.genome -w 100 | awk '{OFS="\t"; print $1,$2,$3,NR}'> hg38_window100bp.bed

# to consider motif boundary cases for 100bp windows, +/- 10bp
#bedtools makewindows -g hg38.genome -w 100 | bedtools slop -b 10 -i - -g hg38.genome | awk '{OFS="\t"; print $1,$2,$3,NR}'> hg38_window100bp_both10bp.bed

#mysql --user=genome --host=genome-mysql.cse.ucsc.edu -A -e \
#        "select chrom, size from mm10.chromInfo" > mm10.genome
## 1000bp windows
#bedtools makewindows -g mm10.genome -w 1000 | awk '{OFS="\t"; print $1,$2,$3,NR}'> mm10_window1kb.bed

## 200bp windows
bedtools makewindows -g mm10.genome -w 200 | awk '{OFS="\t"; print $1,$2,$3,NR}'> mm10_window200bp.bed

## 100bp windows
#bedtools makewindows -g mm10.genome -w 100 | awk '{OFS="\t"; print $1,$2,$3,NR}'> mm10_window100bp.bed
#
## to consider motif boundary cases for 100bp windows, +/- 10bp
#bedtools makewindows -g mm10.genome -w 100 | bedtools slop -b 10 -i - -g mm10.genome | awk '{OFS="\t"; print $1,$2,$3,NR}'> mm10_window100bp_both10bp.bed
