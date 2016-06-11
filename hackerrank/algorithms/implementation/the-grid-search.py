#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)
    if r > R or c > C or r <=0 or c <= 0:
        print 'NO'
        continue
    found = False
    for i in range(R-r+1):
        indices = []
        for j in range(C-c+1):
            if G[i][j] == P[0][0]:
                idx = G[i].find(P[0], j)
                if idx != -1:
                    indices.append(idx)
        #print indices
        for start in indices:
            ans = [start]
            for k in range(1, r):
                idx = G[i+k].find(P[k], start)
                if idx == -1 or idx != start:
                    continue
                else:
                    ans.append(idx)
            if len(ans) == r:
                found = True
                break
        if found:
            break
    print 'YES' if found else 'NO'
