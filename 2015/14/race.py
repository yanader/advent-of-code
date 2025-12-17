from reindeer import Reindeer
from helpers import *


data = importFile("input.txt")

maxDistance = 0
raceLength = 2503

for line in data:
    r = createReindeer(line)
    distance = r.race(raceLength)
    if distance > maxDistance:
        maxDistance = distance

print(maxDistance)