#unsolved

import p07

# def circular_primes(below: int):
#     "find the number of circular primes below a certain number"

#     #search for a prime, turn it into a string and then test to see if the opposite of it is a prime

#     prime_list = p07.find_primes_below(below)
#     print(prime_list)
#     total_circular_primes = 0 # this accounts for our logic ruling out 2 as a prime
#     for prime in prime_list:
#         print("prime: " + str(prime))
#         string = str(prime)
#         if len(string)==1:
#             total_circular_primes += 1
#             continue
#         if string.__contains__("0"): continue
#         if string.__contains__("2"): continue
#         if string.__contains__("4"): continue
#         if string.__contains__("6"): continue
#         if string.__contains__("8"): continue
#         if len(string)==2:
#             inverse = string[1] + string[0]
#             if prime_list.__contains__(int(inverse)): 
#                 print(prime)
#                 total_circular_primes += 1
#                 continue
#         if len(string)==3:
#             inverse1 = string[0] + string[1]
#     return total_circular_primes

# print(circular_primes(100))

# need to create a nested for loop that can calculate all of the permutations of number.

# create a new string with the last character appended to the front of the new string.  Do this LENGTH amount of times on each number.

# for x in primes:
    # for len(x):
        # new_string = string[-1] + string[1,-1]


def circle_primes(below: int):
    prime_list = p07.find_primes_below(below)
    circular_list = []
    for prime in prime_list:
        string = str(prime)
        new_string = string
        ct = 1
        is_circular = True
        if len(string) !=1:
            if string.__contains__("0"): continue
            if string.__contains__("2"): continue
            if string.__contains__("4"): continue
            if string.__contains__("6"): continue
            if string.__contains__("8"): continue
        while ct < len(string):
            new_string = new_string[-1] + new_string[0:-1]
            bool = prime_list.__contains__(int(new_string))
            if bool == False: 
                is_circular = False
                break
            ct += 1 
        if is_circular: 
            print("Adding prime: " + str(prime))
            circular_list.append(prime)

    return circular_list
            
test = circle_primes(1000000)
print(len(test))



        
        
        