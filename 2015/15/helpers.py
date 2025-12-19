from ingredients import Ingredients
import re

def importFile(filename):
    with open(filename, "r") as f:
        data = [line.strip() for line in f]
    return data

def createIngredient(line):
    parts = re.split(r'[ ,]', line)
    return Ingredients(parts[0][0:-1],int(parts[2]),int(parts[5]),int(parts[8]),int(parts[11]), int(parts[14]))





