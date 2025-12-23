with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.read().split(",")]

position = ['N',0,0] # Direction, X, Y
visited = [[0,0]]

def turn(facing, turning):
    if facing == "N" and turning == "L": return "W"
    if facing == "N" and turning == "R": return "E"
    if facing == "S" and turning == "L": return "E"
    if facing == "S" and turning == "R": return "W"
    if facing == "E" and turning == "L": return "N"
    if facing == "E" and turning == "R": return "S"
    if facing == "W" and turning == "L": return "S"
    if facing == "W" and turning == "R": return "N"

def move(position, move, visited):
    ...

#  The problem to solve here is that I am visiting a site as I step square by square but the below doesn't capture that
    
for move in data:
    position[0] = turn(position[0], move[0])
    if position[0] == "N":
        for i in range(int(move[1:])):
            position[1] += 1
            newLocation = [position[1],position[2]]
            if newLocation in visited:
                print(newLocation)
                break
            else:
                visited.append(newLocation)
    if position[0] == "S":
        for i in range(int(move[1:])):
            position[1] -= 1
            newLocation = [position[1],position[2]]
            if newLocation in visited:
                print(newLocation)
                break
            else:
                visited.append(newLocation)
    if position[0] == "E":
        for i in range(int(move[1:])):
            position[2] += 1
            newLocation = [position[1],position[2]]
            if newLocation in visited:
                print(newLocation)
                break
            else:
                visited.append(newLocation)
    if position[0] == "W":
        for i in range(int(move[1:])):
            position[2] -= 1
            newLocation = [position[1],position[2]]
            if newLocation in visited:
                print(newLocation)
                break
            else:
                visited.append(newLocation)


