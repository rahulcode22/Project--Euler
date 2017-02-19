def ispalindrome(n):
    s=str(n)
    return s==s[::-1]
def smallerpalindrome(n):
    max=-2**31
    for i in xrange(999,99,-1):
        for j in xrange(999,i-1,-1):
            mul=j*i
            if mul>n:
                continue
            if mul<max:
                break
            if isplaindrome(mul) and mul<n:
                max=mul
    return max
t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    print smallerpalindrome(n)
