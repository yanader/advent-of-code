from helpers import *

data = importFile("input.txt")

# print(MESSAGE)

for line in data:
    sue = sueBuilder(line)
    checker = 0
    for key in sue.details.keys():
        if sue.details[key] == MESSAGE[key]:
            checker += 1
    if checker == 3:
        print(sue.number)


