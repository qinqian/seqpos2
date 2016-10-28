#!/bin/bash


for i in cistrome/*
do
   if [ ! -s ${i}.100bp ]
   then
      python bin/seqpos2 -f hg38_window1kb.fa -p $i -o ${i}.100bp
   fi
done
