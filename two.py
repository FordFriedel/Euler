#solved
#2/27/22

first = 1
second = 1

def two(older, old, sum):

    if(old >= 4000000):
        return sum
    new = older + old
    if((new%2) == 0):
        sum += new
    return two(old, new, sum)

print(two(first,second,0))