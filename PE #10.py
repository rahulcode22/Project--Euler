
def sieve(n):
    n=n+1
    a=[True]*n
    a[0]=False
    a[1]=False
    s=0
    for i in range(2,int(n**0.5)+1):
        if a[i] is True:
            for j in range(i**2,n,i):
                a[j]=False
    for i in range(0,len(a)):
        if a[i]:
            s +=i
        
    return s 


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print sieve(n)
