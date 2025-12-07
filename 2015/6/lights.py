
def decorate(fileName):
    N = 1000
    display = [[0 for i in range(N)] for j in range(N)]
    with open(fileName, "r") as file:
        for line in file:
            coords = defineRangeFromString(line)
            if instruction(line) == "on":
                switchOn(display, coords)
            elif instruction(line) == "off":
                switchOff(display, coords)
            if instruction(line) == "tog":
                toggle(display, coords)
    
    totalBrightness = 0
    for row in display:
        for light in row:
            totalBrightness += light
    
    print(totalBrightness)


def switchOn(lights, coords):
    # Switch on all lights in an array
    for j in range(coords[0], coords[2] + 1):
        for i in range(coords[1], coords[3] + 1):
            lights[i][j] += 1

def switchOff(lights, coords):
    # Switch off all lights in an array
    for j in range(coords[0], coords[2] + 1):
        for i in range(coords[1], coords[3] + 1):
            if lights[i][j] > 0:
                lights[i][j] -= 1

def toggle(lights, coords):
    # Toggle all lights in an array
    for j in range(coords[0], coords[2] + 1):
        for i in range(coords[1], coords[3] + 1):
            lights[i][j] += 2

def instruction(s):
    if s.startswith("turn on"):
        return "on"
    if s.startswith("turn off"):
        return "off"
    if s.startswith("toggle"):
        return "tog"

def defineRangeFromString(s):
    # return a numeric representation of the coordinates in an instruction
    words = s.split(" ")
    topLeft = words[-3].split(",")
    bottomRight = words[-1].split(",")
    return (int(topLeft[0]), int(topLeft[1]), int(bottomRight[0]), int(bottomRight[1]))

    

# testString = "turn off 150,300 through 213,740"

decorate("input.txt")