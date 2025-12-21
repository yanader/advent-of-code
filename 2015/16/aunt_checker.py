from helpers import *


def auntOne():
    data = importFile("input.txt")

    for line in data:
        sue = sueBuilder(line)
        checker = 0
        for key in sue.details.keys():
            if sue.details[key] == MESSAGE[key]:
                checker += 1
        if checker == 3:
            print(sue.number)


def auntTwo():
    data = importFile("input.txt")

    for line in data:
        sue = sueBuilder(line)
        checker = 0
        for key in sue.details.keys():
            if key == "cats" or key == "trees":
                if sue.details[key] > MESSAGE[key]:
                    checker += 1
            elif key == "pomeranians" or key == "goldfish":
                if sue.details[key] < MESSAGE[key]:
                    checker += 1
            else:
                if sue.details[key] == MESSAGE[key]:
                    checker += 1
        if checker == 3:
            print(sue.number)

auntTwo()



