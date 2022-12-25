#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.

#solved
#2/27/22
#solution: 4613732

first = 1
second = 1

def fibonacci_iterate(older: int, old: int, sum: int, max: int):
    "find the sum of the even valued term of a fibonacci sequence"
    if(old >= max):
        return sum
    new = older + old
    if((new%2) == 0):
        sum += new
    return fibonacci_iterate(old, new, sum, max)

def fibonacci_even_sum(max: int):
    "find the sum of the even valued term of a fibonacci sequence"
    return fibonacci_iterate(1,1,0,max)

if __name__ == "__main__":
    solution = fibonacci_even_sum(4000000)
    print("solution: " + str(solution))

