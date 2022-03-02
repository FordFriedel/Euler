#solved
#3/2/22

from math import sqrt

fail = False

for cSquared in range(1,1000000):

    #if a is a square continue
    if(sqrt(cSquared)%1 == 0):
        print("testing c^2: " + str(cSquared))


        for aSquared in range(1,cSquared + 1):
            if(sqrt(aSquared)%1 == 0):
                b = 1000 - sqrt(cSquared) - sqrt(aSquared)

                if(b**2 + aSquared == cSquared):
                    print(b * sqrt(cSquared) * sqrt(aSquared))
                    fail = True
                    break
        if(fail):
            break
