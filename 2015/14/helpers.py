from reindeer import Reindeer

def importFile(filename):
    with open(filename, "r") as f:
        data = [line.strip().split(" ") for line in f]
    return data

def createReindeer(line):
    return Reindeer(line[0],int(line[3]),int(line[6]),int(line[13]))
