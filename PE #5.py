from fraction import gcd
def multiple(n):
    max=reduce(lambda i,j:i*j/gcd(i,j),range(1,n+1))
    print max
        
