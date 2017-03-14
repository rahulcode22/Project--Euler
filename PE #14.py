#Program 1 for computing collatz sequence
coll={1:1}
def sequence(coll,n):
    if not coll.get(n,0):
        if n%2:
            coll[n]=1+sequence(coll,3*n+1)
        else:
            coll[n]=1+sequence(coll,n/2)
    return coll[n]
t=int(raw_input())
for i in range(t):
    N=int(raw_input())
    m,n=0,0
    for i in range(1,N+1):
        c=sequence(coll,i)
        if c>m:
            m,n=c,i
    print n
    
    
#Program 2 
c = [1, 2, 3, 6, 7, 9, 18, 19, 25, 27, 54, 55, 73, 97, 129, 171, 231, 235, 313, 327, 649, 654,
     655, 667, 703, 871, 1161, 2223, 2322, 2323, 2463, 2919, 3711, 6171, 10971, 13255, 17647, 
     17673, 23529, 26623, 34239, 35497, 35655, 52527, 77031, 106239, 142587, 156159, 216367, 
     230631, 410011, 511935, 626331, 837799, 1117065, 1126015, 1501353, 1564063, 1723519, 
     2298025, 3064033, 3542887, 3732423, 5649499, 6649279, 8400511, 11200681]
t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    print min(c[::-1], key=lambda x: x>n)
