
import  numpy  as np 
from scipy.stats import spearmanr
from glob import glob

def load(x):
    score = []
    with open(x) as inf:
        for line in inf:
            line = line.strip().split()
            score.append(float(line[-1]))
    return np.array(score)

ns = glob('*100bp')
for index, i in enumerate(ns):
    for index_j, j in enumerate(ns[(index+1):]):
        x = load(i)
        y = load(j)
        ir = spearmanr(x, y)
        print i,j,ir[0],ir[1]
