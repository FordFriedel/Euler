#solved
#2/27/22

# take num
# while solved == false
# as x increases
# if num % x == 0
# test if num / x is prime
# if it is solved = true

from math import sqrt


def primeFactor(num):
    # for every number between 2 and the number we are looking to find the largest prime number in
    for x in range(2,num):

        #enter if the test case finds a whole number
        if num%x == 0: 
            testNum = num/x
            isPrime = True

            # for every number between 2 and half of the test number
            for i in range(2,int((testNum)/2)):

                # if testNum has a factor. we want to break
                if(testNum%i == 0):
                    isPrime = False 
                    break

            #if there are no factors in the test number we know it is a prime
            if(isPrime):
                return testNum

print(int(primeFactor(600851475143)))
