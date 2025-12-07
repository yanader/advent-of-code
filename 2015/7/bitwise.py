from helpers import *

charToSolve = 'a'
fileInput = "input.txt"


instructions = {}
resolveStack = [charToSolve]
with open(fileInput, "r") as file:
    for line in file:
        parts = line.rstrip().split("->")
        instructions[parts[1].strip()] = [parts[0].strip(), False, ""]

while len(resolveStack) != 0:
    if canResolve(resolveStack[-1], instructions):
        ...
        # Resolve the item.
        resolve(resolveStack[-1], instructions)

        # Remove it from the resolve stack.
        resolveStack.pop()
    else:
        for _ in dependents(resolveStack[-1], instructions):
            if _ in instructions:
                resolveStack.append(_)

print(instructions[charToSolve])

answer = instructions[charToSolve][2]

resolveStack = [charToSolve]
for i in instructions:
    instructions[i][1] = False
    instructions[i][2] = ""

instructions['b'][1] = True
instructions['b'][2] = answer

while len(resolveStack) != 0:
    if canResolve(resolveStack[-1], instructions):
        ...
        # Resolve the item.
        if instructions[resolveStack[-1]][1] == False:
            resolve(resolveStack[-1], instructions)

        # Remove it from the resolve stack.
        resolveStack.pop()
    else:
        for _ in dependents(resolveStack[-1], instructions):
            if _ in instructions:
                resolveStack.append(_)

print(instructions[charToSolve])