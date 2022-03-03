#unsolved
#3/2/22'

from math import sqrt

total = 1
for x in range(1,2000001,2):
    isPrime = True
    if(x%2 != 0):
        print("testing: " + str(x))
        for y in range(3,int(sqrt(x)),2):
            if(x%y == 0):
                isPrime = False
                break
        if(isPrime):
            total += x
print(total)