NOT = lambda a: ~a & 0xFFFF
AND = lambda a, b: a & b 
OR = lambda a, b: a | b 
XOR = lambda a, b: a ^ b & 0xFFFF
LSHIFT = lambda a, x: (a << x) & 0xFFFF
RSHIFT = lambda a, x: (a >> x) & 0xFFFF
PASS = lambda a: (a) & 0xFFFF

def instructionSwitch(s):
    if "NOT" in s: return "NOT"
    if "AND" in s: return "AND"
    if "OR" in s: return "OR"
    if "XOR" in s: return "XOR"
    if "LSHIFT" in s: return "LSHIFT"
    if "RSHIFT" in s: return "RSHIFT"
    return "PASS"

def canResolve(item, instructions):
    instruction = instructions[item][0]
    parts = instruction.split(" ")

    if not operatorInInst(instruction) and instructionNumeric(instruction):
        return True

    for part in parts:
        if part in instructions and instructions[part][1] == False:
            return False
    return True

def instructionNumeric(inst):
    for item in inst:
        if not(item.isnumeric()):
            return False
    return True

def operatorInInst(inst):
    operators = ['NOT','AND','OR','XOR','LSHIFT','RSHIFT']
    for operator in operators:
        if operator in inst:
            return True
    return False

def dependents(item, instructions):
    instruction = instructions[item][0]
    parts = instruction.split(" ")
    newItems = []
    for part in parts:
        if part not in ['NOT','AND','OR','XOR','LSHIFT','RSHIFT']:
            newItems.append(part)
    return newItems

def resolve(item, instructions):
    command = instructions[item][0]
    operation = instructionSwitch(command)
    deps = dependents(item, instructions)
    values = valuesBuilder(deps, instructions)
    if operation == "NOT":
        instructions[item][2] = NOT(values[0])
    elif operation == "AND":
        instructions[item][2] = AND(values[0], values[1])
    elif operation == "OR":
        instructions[item][2] = OR(values[0], values[1])
    elif operation == "RSHIFT":
        instructions[item][2] = RSHIFT(values[0], values[1])
    elif operation == "LSHIFT":
        instructions[item][2] = LSHIFT(values[0], values[1])
    elif operation == "PASS":
        instructions[item][2] = values[0]

    instructions[item][1] = True

def valuesBuilder(deps, instructions):
    for i in range(len(deps)):
        if(deps[i].isnumeric()):
            deps[i] = int(deps[i])
        else:
            deps[i] = int(instructions[deps[i]][2])
    return deps

