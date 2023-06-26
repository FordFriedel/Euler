#solved
#6/25/23

import math

def find_tph():
    #find the next number that is triangular, pentagonal and hexagonal
    n = 0
    solved = False
    while solved == False:
        n += 1
        #get next hexagonal num
        h = n * ((2 * n) - 1)

        #test to see if it is pentagonal
        p = (1 + math.sqrt(24*h + 1))/6
        if(p - int(p) != 0):
            continue

        #test to see if it is triangular
        t = math.sqrt(8 * (h) + 1)
        if(t - int(t) != 0):
            continue
        
        print(str(h))
        

        if(n>=1000):
            return
        
find_tph()

    
        

    



