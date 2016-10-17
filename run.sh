#!/bin/bash


for i in cistrome/*
do
   if [ ! -s ${i}.1kb ]
   then
      python bin/seqpos2 -f hg38_window1kb.fa -p $i -o ${i}.1kb
   fi
done
