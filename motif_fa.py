import sys,os,unittest
import numpy as np
from mdseqpos import _seq

## scan motif whole genome , need binoch package, numpy , input like:
#### python motif_genome.py hg19 peak.bed pwm.txt output_motifsite.bed
def scan(fa, pssmf):
        #seqs = ["ACTGATATACTGATACTGCGCGCCAGTGCGCGCGACTGACCAGTACACACACACACC"]
        #["ATATATATATACGCGCGCGCGCGCGACACACACACACACACACACACAC",\
        #"ATATATATATACTCGCGCGCGCGCGACACACACACACACACACACACAC",\
        #"ATATATATATACTGGCGCGCGCGCGACACACACACACACACACACACAC",\
        #"ACTGGGGTACTGAGGCGCGCGCGCGACACACACACACACACACACACAC",\
        #"ATATATATATACGCGCGCGCGCGCGACACACAGTACACACACCCCCAGT",\
        #"ACTGATATACTGATACTGCGCGCGCGCGCGACACACACACACACACACC",\
        #"ACTGATATACTGATACTGCGCGCGCGCGCGACTGACACACACACACACC"]
        #prob = seq.count.count(seqs)
        fas = []
        fid = []
        n = 0
        with open(fa) as inf:
                for line in inf:
                        if n % 2 == 0:
                                fid.append(line.strip()[1:])
                        else:
                                fas.append(line.strip())
                        n += 1

        option = _seq.CUTOFF_OPTION
        order = 2
        pssm = np.loadtxt(pssmf)
        outf1 = open(fa + '.motif','w')
       # outf2 = open(out2,'w')
        #start_t    = [0]#[26,10,10,0,45,0,0]
        #end_t      = [4]#[30,14,14,4,49,4,4]
        #strand_t   = [0]#[1,0,0,0,1,0,0]
        #pssm = numpy.array( [ [1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0] ] ,numpy.float )
        for i in range(len(fas)):
            idxmax,startmax,endmax,orientmax,scoremax = _seq.seqscan( [fas[i]], pssm, [], order, 0 )
            # print(fas[i])
            m = 0
            for j in range(len(startmax)):
                    if scoremax[j] > m:
                            m = scoremax[j]
            print >>outf1, fid[i]+'\t'+str(m)
                # if startmax[j] < 100 :
                #     continue
                #realstart = start + startmax[j]
                #realend = start + endmax[j]
                #if end - realend < 100:
                #    continue
                #realscore = str(scoremax[j])
                #realorient = orientmax[j]
                #realseq = seqs[0][int(startmax[j]):int(endmax[j])]                
                #if float(realscore) < 1000 : 
                #    continue
                #if realorient == 0:
                #    ll = [chrm,str(realstart-1),str(realend-1),realseq,realscore,"+"]
                #    newline = "\t".join(ll)+"\n"
                #    outf1.write(newline)
                #elif realorient == 1:
                #    #print realstart-1,realend-1,realseq
                #    ll = [chrm,str(realstart-1),str(realend-1),realseq,realscore,"-"]
                #    newline = "\t".join(ll)+"\n"
                #    outf1.write(newline)
                #else:
                #    print "error"
        outf1.close()

import argparse

p = argparse.ArgumentParser('')
p.add_argument('-fa')
p.add_argument('-pssm')
args = p.parse_args()
scan(args.fa, args.pssm)

