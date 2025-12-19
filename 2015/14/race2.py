from reindeer import Reindeer
from helpers import *


data = importFile("input.txt")

maxDistance = 0
raceLength = 2503

scores = {}
reindeer = []

for line in data:
    r = createReindeer(line)
    scores[r.name] = 0
    reindeer.append(r)



for i in range(2504):
    roundDistances = {}
    for r in reindeer:
        distance = r.race(i + 1)
        roundDistances[r.name] = distance
    res = max(roundDistances, key=lambda k: roundDistances[k])
    scores[res] += 1
    
    


print(scores)