#!/bin/python

import sys
def conversion(x):
    res=1
    for i in x:
        res=res*int(i)
    return res
def substring(num,k):
    results=[]
    for i in range(len(num)-k+1):
        results.append(conversion(num[i:k+i]))
    return results
        

        
        

t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = raw_input().strip()
    print max(substring(num,k))
