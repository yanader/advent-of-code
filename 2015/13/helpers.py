def processInstruction(i):
    instruction = i.rstrip().split(" ")
    first = instruction[0]
    last = instruction[-1][0:-1]
    amount = int(instruction[3])
    if instruction[2].lower() == "lose":
        amount *= -1
    return (first, amount, last)

def personList(instructions):
    people = []
    for i in instructions:
        line = i.split(" ")
        if line[0] not in people:
            people.append(line[0])
    return people


def seatingArrangementHappiness(arrangement, details):
    happiness = 0
    for i in range(len(arrangement) - 1):
        happiness += neighbourHappiness(arrangement[i], arrangement[i + 1], details)
    happiness += neighbourHappiness(arrangement[-1], arrangement[0], details)
    return happiness

def neighbourHappiness(personOne, personTwo, details):
    happiness = 0
    for d in details:
        if personOne in d and personTwo in d:
            happiness += d[1]
    return happiness    