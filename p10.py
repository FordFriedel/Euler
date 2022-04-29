#solved
#3/2/22
#solution: 142913828922

from math import sqrt

def find_primes(limit: int):
    "returns a list of primes below the specified number (exclusive)"
    if limit < 3:
        return [2]
    primes = [2]
    for test in range (3,limit,2):
        isPrime = True
        for prime in primes:
            if(prime >= sqrt(test)+1):
                break
            if(test % prime == 0):
                isPrime = False
                break
        if(isPrime):
            primes.append(test)
    return primes

if __name__ == "__main__":
    array = find_primes(2000000)
    total = 0
    for prime in array:
        total += prime
    print(total)

