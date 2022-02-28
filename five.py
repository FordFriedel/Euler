#solved
#2/28/22

def five():
    x = 0
    solved = False
    while solved == False:
        x += 46189
        for y in range(1,21):
            if(x%y!=0):
                print("broken at: " + str(x))
                break

            if(y == 20):
                solved = True
                return x

print(five())
        
#this can be solved with no programming at all
#find the prime factorization of all the factors:
# 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232,792,560

