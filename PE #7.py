T = int(input().strip())
a = [int(input().strip()) for _ in range(T)]

N = max(a)

sz = N * int(math.log(N) + int(math.log(math.log(N)) + 6))

arr = [True for _ in range(sz)]
primes = []

i = 2
while i < sz:
    if arr[i]:
        primes.append(i)
        for j in range(2, (sz-1)//i + 1):
            arr[i*j] = False
    i += 1
    
for idx in a:
    print(primes[idx-1])
