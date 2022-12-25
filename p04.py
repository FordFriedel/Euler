#Find the largest palindrome made from the product of two 3-digit numbers.

#solved
#2/28/22
#solution: 906609

#goal is to find the largest palindrome number from the product of two 3 digit numbers
#999 * 999 is 6 digits
#I think I find palindromes and then look for their products
#start high and go back downwards

def six_digit_palindrome():
    "find the largest palindrome number from the product of two 3 digit numbers"
    largest = 0
    i = 9
    j = 9
    k = 9
    while i >= 0:
        first = i * 100000
        sixth = i * 1
        i -= 1
        j = 9
        while j >= 0:
            second = j * 10000
            fifth = j * 10
            j -= 1
            k = 9
            while k >= 0:
                third = k * 1000
                fourth = k * 100
                k -= 1
                num = first + second + third + fourth + fifth + sixth
                print(num)
                for x in range(100,1000):
                    if((num%x)==0):
                        if(num/x < 1000):
                            if(num > largest):
                                print("new largest " + str(num))
                                print(x)
                                largest = num
    return largest

if __name__ == "__main__":       
    solution = six_digit_palindrome()
    print("solution: " + solution)



