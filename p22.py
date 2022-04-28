#solved
#4/28/2022

alphaDict = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26,
    }

with open('files/names.txt','r') as file:
    names = file.readline()
    names2 = names.split(",")
names2.sort()


total = 0
index = 1
for name in names2:
    print(name)
    nameTotal = 0
    for char in name:
        char = char.lower()
        if char!="\"":
            nameTotal += alphaDict[char]
    total += nameTotal * index
    index += 1

print(total)
