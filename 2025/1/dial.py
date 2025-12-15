with open("input.txt", "r") as f:
    data = [line.strip() for line in f]

position = 50
zeroCount = 0
passedZeroCount = 0

def zeroHits(position, turn, direction):
    if direction == "L":
        first_hit = position if position != 0 else 100
    else:  # "R"
        first_hit = (100 - position) if position != 0 else 100

    if turn < first_hit:
        return 0

    remaining = turn - first_hit
    return 1 + (remaining // 100)

for turn in data:
    direction = turn[0]
    rotationalAmount = int(turn[1:])
    if direction == "L":
        passedZeroCount += zeroHits(position, rotationalAmount, direction)
        position -= rotationalAmount
        if position < 99:
            position = position % 100
    elif direction == "R":
        passedZeroCount += zeroHits(position, rotationalAmount, direction)
        position += rotationalAmount
        if position > 99:
            position = position % 100
    if position == 0:
        zeroCount += 1

# for turn in data:
#     direction = turn[0]
#     rotationalAmount = int(turn[1:])
#     if direction == 'L':
#         for i in range(rotationalAmount):
#             position -= 1
#             if position == 0: passedZeroCount += 1
#             if position == -1: position = 99
#     if direction == 'R':
#         for i in range(rotationalAmount):
#             position += 1
#             if position == 100: position = 0
#             if position == 0: passedZeroCount += 1

# 6228 is correct
print(passedZeroCount)
    
