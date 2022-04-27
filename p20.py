#unsolved
#4/27/22

def sumDigits(x):
    prod = x
    sum = 0
    while x > 1:
        x-=1
        prod *= x
    while prod > 0:
        sum += prod % 10 
        prod = prod // 10
    return sum

print(sumDigits(100))