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
        