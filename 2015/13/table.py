with open("input.txt", "r") as f:
    data = [line.strip() for line in f]

# print(data)

def processInstruction(i):
    instruction = i.rstrip().split(" ")
    first = instruction[0]
    last = instruction[-1][0:-1]
    amount = int(instruction[3])
    if instruction[2].lower() == "lose":
        amount *= -1
    return (first, amount, last)


for d in data:
    print(processInstruction(d))