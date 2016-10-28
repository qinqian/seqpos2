#!/bin/bash


for i in cistrome/*pwm
do
   if [ ! -s ${i}.100bp ]
   then
      python bin/seqpos2 -f  hg38_window100bp_both10bp.fa -p $i -o ${i}.100bp
   fi
done
