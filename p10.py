#solved
#3/2/22

from math import sqrt

primes = [2]

total = 0
for x in range(3,2000000,2):
    isPrime = True
    
    for y in primes:
        if(y >= sqrt(x)+1):
            break
        if(x%y == 0):
            isPrime = False
            break
    if(isPrime):
        primes.append(x)
for prime in primes:
    total += prime
print(total)