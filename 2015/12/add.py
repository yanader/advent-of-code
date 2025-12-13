import json
from helpers import *

data = load_list("input.json")

def addNums(lst):
    sum = 0
    for _ in lst:
        if type(_) is list:
            sum += addNums(_)
        elif type(_) is dict:
            sum += addNums(_.values())
        elif isinstance(_, int):
            sum += int(_)
    return sum

def addNumsIgnoreRed(lst):
    sum = 0
    for _ in lst:
        if type(_) is list:
            sum += addNumsIgnoreRed(_)
        elif type(_) is dict and not(dictContainsRed(_)):
            sum += addNumsIgnoreRed(_.values())
        elif isinstance(_, int):
            sum += int(_)
    return sum

def dictContainsRed(dct):
    return 'red' in dct or 'red' in dct.values()

test = [1,"red",5]

print(addNumsIgnoreRed(data))
