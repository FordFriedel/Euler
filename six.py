#solved
#2/28/22

sumOfSquares = 0
squareOfSum = 0
for i in range(1,101):
    squareOfSum += i
    sumOfSquares += i**2
squareOfSum = squareOfSum ** 2
print(str(sumOfSquares - squareOfSum))

