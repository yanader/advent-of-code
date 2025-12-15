with open("input.txt", "r") as f:
    data = [line.strip() for line in f]

position = 50
zeroCount = 0

for turn in data:
    if turn[0] == "L":
        position -= int(turn[1:])
        if position < 99:
            position = position % 100
    elif turn[0] == "R":
        position += int(turn[1:])
        if position > 99:
            position = position % 100
    if position == 0:
        zeroCount += 1

print(zeroCount)
    


