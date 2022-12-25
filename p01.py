#Find the sum of all the multiples of 3 or 5 below 1000

#solved
#2/25/22
#solution: 233168

def one(x): #so specific not even worth making into a reusable function
    ptr = 0
    total = 0
    while ptr < x:
        if((ptr%3) == 0 or (ptr%5) == 0):
            total += ptr
        ptr += 1
    print(total)

one(1000)