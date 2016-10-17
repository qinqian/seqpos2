#!/usr/bin/env python

import numpy as np
import os
import h5py
import glob

motifs = glob.glob('cistrome/*1kb')
print(motifs)

with h5py.File('hg38_seqpos2.h5', 'w') as store:
    for m in motifs:
        print(m)
        score = []
        with open(m) as inf:
            for l in inf:
                l = l.strip().split()
                score.append(l[1])
        scores = np.array(score, dtype=np.float32)
        store[os.path.basename(m).replace('.pwm.1kb', '')] = scores

