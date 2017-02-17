import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    lis=[]
    a,b=0,1
    
    while b<n:
        a,b=b,a+b
        if a%2==0:
            lis.append(a)
        
    s=sum(list(lis))   
    print s
    
        
