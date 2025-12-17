from itertools import permutations
from helpers import *

with open("input.txt", "r") as f:
    data = [line.strip() for line in f]


pairDetails = []

for d in data:
    pairDetails.append(processInstruction(d))

people = personList(data)

for person in people:
    pairDetails.append(('ste',0,person))
    pairDetails.append((person,0,'ste'))


people.append("ste")

print(people)
print(pairDetails)

p = permutations(people)
p = list(p)

highestHappiness = 0

for _ in p:
    newHappiness = seatingArrangementHappiness(_, pairDetails)
    if newHappiness > highestHappiness:
        highestHappiness = newHappiness


print(highestHappiness)