
def housesVisited(fileName):
    houses = {}
    x_pos = 0
    y_pos = 0
    houses[0] = [0]

    with open(fileName, "r") as file:
        for line in file:
            for _ in line:
                if _ == '^':
                    y_pos += 1
                elif _ == 'v':
                    y_pos -= 1
                elif _ == '<':
                    x_pos -= 1
                elif _ == '>':
                    x_pos += 1
                
                if x_pos not in houses:
                    houses[x_pos] = [y_pos]
                elif y_pos not in houses[x_pos]:
                    houses[x_pos].append(y_pos)

    visitCount = 0
    for x in houses:
        visitCount+=len(houses[x])
    
    return visitCount

def housesVisitedYearTwo(fileName):
    houses = {}
    x_pos_santa = 0
    y_pos_santa = 0
    x_pos_robo = 0
    y_pos_robo = 0
    tracker = 0
    houses[0] = [0]

    with open(fileName, "r") as file:
        for line in file:
            for _ in line:
                if tracker % 2 == 0:
                    if _ == '^':
                        y_pos_santa += 1
                    elif _ == 'v':
                        y_pos_santa -= 1
                    elif _ == '<':
                        x_pos_santa -= 1
                    elif _ == '>':
                        x_pos_santa += 1
                    if x_pos_santa not in houses:
                        houses[x_pos_santa] = [y_pos_santa]
                    elif y_pos_santa not in houses[x_pos_santa]:
                        houses[x_pos_santa].append(y_pos_santa)
                    tracker+=1
                else:
                    if _ == '^':
                        y_pos_robo += 1
                    elif _ == 'v':
                        y_pos_robo -= 1
                    elif _ == '<':
                        x_pos_robo -= 1
                    elif _ == '>':
                        x_pos_robo += 1
                    if x_pos_robo not in houses:
                        houses[x_pos_robo] = [y_pos_robo]
                    elif y_pos_robo not in houses[x_pos_robo]:
                        houses[x_pos_robo].append(y_pos_robo)
                    tracker+=1

    visitCount = 0
    for x in houses:
        visitCount+=len(houses[x])
    
    return visitCount


fileName = "input.txt"

print(housesVisited(fileName))
print(housesVisitedYearTwo(fileName))

