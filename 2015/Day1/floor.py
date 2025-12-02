
def finalFloor(fileName):
    floor = 0
    with open(fileName, "r") as file:
        for line in file:
            for _ in line:
                if _ == "(":
                    floor+=1
                elif _ == ")":
                    floor-=1
    return floor

def firstBasementVisit(file):
    floor = 0
    index = 1
    with open(file, "r") as f:
        for line in f:
            for _ in line:
                if _ == "(":
                    floor+=1
                elif _ == ")":
                    floor-=1
                if floor == -1:
                    return index
                else:
                    index+=1

fileName = "input.txt"

print(finalFloor(fileName))
print(firstBasementVisit(fileName))
