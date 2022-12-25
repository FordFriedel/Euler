# starting with the number 1 and moving to the right in a closckwise direction a 5 by 5 spiral is formed as follows

#It can be verified that the sum of the numbers on  the diagonals is 101 (5x5 square)

# What is the sum of numbres in a 1001 by 1001 spiral

def spiral_diagonals(length):
    "find the sum of the diagonals in a grid"
    # 5x5 should equal 101

    sum = 1
    placeholder = 1
    side_length = 1
    while side_length < length:
        side_length += 2
        sum = sum + placeholder + side_length -1
        placeholder = placeholder + side_length -1
        print(sum)
        sum = sum + placeholder + side_length -1
        placeholder = placeholder + side_length -1
        print(sum)
        sum = sum + placeholder + side_length -1
        placeholder = placeholder + side_length -1
        print(sum)
        sum = sum + placeholder + side_length -1
        placeholder = placeholder + side_length -1
        print(sum)
    return sum

    

spiral_diagonals(5)
print(spiral_diagonals(1001))




# 21 22 23 24 25
# 20 7  8  9  10
# 19 6  1  2  11
# 18 5  4  3  12
# 17 16 15 14 13
        
# total = 1 + (3 + 5 + 7 + 9) + (13 + 17 + 21 + 25)

#1 + (last operator + sidelength - 1)

# 1 + 1 + 2 = 4
# 4 + 3 + 2 = 9
# 9 + 5 + 2 = 16
# 16 + 7 + 2 = 25
# 25 + 9 + 4 = 

# 
# 1 + (1 + 2) = 4
# 4 + (4 + 2) = 10 need to be at 9
# 10 + 10 + 2 = 22 need to be at 16