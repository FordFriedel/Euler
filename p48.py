#solved
#6/25/23

def self_powers(sum, num, limit):
    #find the sum of the products of the powers for their respect number idk man
    if(num > limit):
        return sum
    #find the sum of the self power
    current_sum = 1
    for x in range(num):
        #print(str(x))
        #print("Current Sum: " + str(current_sum))
        current_sum = current_sum * num

    return self_powers(current_sum + sum,num + 1,limit)
    #add it to the toal, iterate further

def self_powers_loop(limit):
    sum = 0
    
    for x in range(1, limit+1):
        current = 1
        for y in range(1, x + 1):
            #print("x: " + str(x) + "| y: " + str(y))
            current = current * x
        sum += current
    return sum


    # #find the sum of the products of the powers for their respect number idk man
    # if(num > limit):
    #     return sum
    # #find the sum of the self power
    # current_sum = 1
    # for x in range(num):
    #     #print(str(x))
    #     #print("Current Sum: " + str(current_sum))
    #     current_sum = current_sum * num

    # return self_powers(current_sum + sum,num + 1,limit)
    # #add it to the toal, iterate further

print("result for 1: " + str(self_powers_loop(1)))
print("result for 2: " + str(self_powers_loop(2)))
print("result for 10  " + str(self_powers_loop(10)))
print("result for 10  " + str(self_powers_loop(1000)))




