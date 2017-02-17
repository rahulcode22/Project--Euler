import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    lis=[]
    for i in range(1,n):
        if (i%3==0):
            lis.append(i)
        elif (i%5==0):
            lis.append(i)
    s=sum(list(lis))
    print s
