### seqpos2
scan a fasta file to output maximum, mean for each sequence, or output the hit.

#### dependency

Get Cython, python develop header, and gcc, bedtools.

#### get your fasta from BED

``` bash
wget -c http://hgdownload.cse.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.masked.gz && gunzip hg38.fa.masked.gz
bedtools getfasta -fi hg38.fa.masked -bed hg38_window1kb.bed -name -fo hg38_window1kb.fa
```

##### built-in cistrome motif database
column order A, C, G, T

#### install

``` bash
python setup.py install --user
or 
sudo python setup.py install 
```


#### example

``` bash
seqpos2  -f test.fa -p cistrome/MC00368.pwm -o test.txt
```
