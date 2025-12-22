def importFile(filename):
    with open(filename, "r") as f:
        data = [int(line.strip()) for line in f]
    return data

TARGET = 150

