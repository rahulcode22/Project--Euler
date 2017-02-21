import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    sumsquare = 0
    sums = 0
    for i in range(1,n+1):
        sumsquare += i**2
        sums += i
    print sums**2 - sumsquare
