#solved
#4/22/22
#solution: 104743

from math import sqrt

primes = [2]
run = True
x = 3
while len(primes) < 10001:
    isPrime = True
    for y in primes:
        if(y >= sqrt(x)+1):
            break
        if(x%y == 0):
            isPrime = False
            break
    if(isPrime):
        primes.append(x)
    x += 1
print(primes[-1])
