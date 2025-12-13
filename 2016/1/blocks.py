with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.read().split(",")]

postition = ['N',0,0]

def turn(facing, turning):
    if facing == "N" and turning == "L": return "W"
    if facing == "N" and turning == "R": return "E"
    if facing == "S" and turning == "L": return "E"
    if facing == "S" and turning == "R": return "W"
    if facing == "E" and turning == "L": return "N"
    if facing == "E" and turning == "R": return "S"
    if facing == "W" and turning == "L": return "S"
    if facing == "W" and turning == "R": return "N"


visited = [[0,0]]

for move in data:
    postition[0] = turn(postition[0], move[0])
    if postition[0] == "N":
        postition[1] += int(move[1:])
    if postition[0] == "S":
        postition[1] -= int(move[1:])
    if postition[0] == "E":
        postition[2] += int(move[1:])
    if postition[0] == "W":
        postition[2] -= int(move[1:])
    location = int(postition[1]),int(postition[2])
    print(location)
    if [location] in visited:
        break
    else:
        visited.append([location])

print(postition)
print(abs(postition[1]) + abs(postition[2]))