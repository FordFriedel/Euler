#solved
#2/25/22

def one(x):
    ptr = 0
    total = 0
    while ptr < x:
        if((ptr%3) == 0 or (ptr%5) == 0):
            total += ptr
        ptr += 1
    print(total)

one(1000)