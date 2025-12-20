from sue import Sue

def importFile(filename):
    with open(filename, "r") as f:
        data = [line.strip() for line in f]
    return data

def sueBuilder(line):
    return Sue(line)

MESSAGE = {"children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1,}