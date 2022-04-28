#solved
#4/22/20

def longest_sequence(x):
    largestSequence = 'None'
    maxLength = 0
    length = 0
    for x in range(x,0,-1):
        y = x
        while y != 1:
            if y%2 == 0:
                y = y/2
            else:
                y = 3 * y + 1
            length += 1
        if length > maxLength:
            maxLength = length
            largestSequence = x
        length = 0
    print(largestSequence)
    print(maxLength)

longest_sequence(1000000)

#837799