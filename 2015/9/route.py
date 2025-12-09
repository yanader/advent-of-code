from itertools import permutations

with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

routeList = []
locations = []

for line in data:
    parts = line.split(" ")
    routeList.append((parts[0], parts[2], int(parts[4])))

for item in routeList:
    if item[0] not in locations:
        locations.append(item[0])
    if item[1] not in locations:
        locations.append(item[1])

p = permutations(locations)
p = list(p)

def tupleDistance(route, routeList):
    distance = 0
    for i in range(len(route) - 1):
        distance += findDistance(route[i], route[i+1], routeList)
    return distance

def findDistance(cityOne, cityTwo, routeList):
    for route in routeList:
        if cityOne in route and cityTwo in route:
            return route[2]

shortestDistance = 1000
longestDistance = 0

for _ in p:
    newDistance = tupleDistance(_, routeList)
    if newDistance < shortestDistance:
        shortestDistance = newDistance
    if newDistance > longestDistance:
        longestDistance = newDistance

print(f"Shortest is: {shortestDistance}")
print(f"Longest is: {longestDistance}")