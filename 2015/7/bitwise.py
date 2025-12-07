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

    