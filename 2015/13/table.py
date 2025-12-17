from itertools import permutations
from helpers import *

with open("input.txt", "r") as f:
    data = [line.strip() for line in f]


pairDetails = []

for d in data:
    pairDetails.append(processInstruction(d))

p = permutations(personList(data))
p = list(p)

highestHappiness = 0

for _ in p:
    newHappiness = seatingArrangementHappiness(_, pairDetails)
    if newHappiness > highestHappiness:
        highestHappiness = newHappiness

print(highestHappiness)