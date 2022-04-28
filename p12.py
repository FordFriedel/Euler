#unsolved
#4/28/22

running = True
index = 1
iteration = 1
while running:
    factors = 0
    test = int(iteration/2)
    for x in range(iteration,1,-1):
        if iteration % x == 0:
            factors += 1
            if factors >= 500:
                print(iteration)
                running = False
                break
    #print("Testing: " + str(iteration) + " Factors: " + str(factors))
    index += 1
    iteration += index

