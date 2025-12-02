

def calcualteArea(x, y):
    return x * y


def calculateSinglePackagePaper(package):
    l = package[0]
    w = package[1]
    h = package[2]
    return (calcualteArea(l, w) * 3) + (calcualteArea(l, h) * 2) + (calcualteArea(w, h) * 2)

def calculateSinglePackageRibbon(package):
    l = package[0]
    w = package[1]
    h = package[2]
    return (l * 2) + (w * 2) + (l * w * h)

def calcualteTotalPaperNeeded(dimensionList):
    total = 0
    for package in dimensionList:
        total+= calculateSinglePackagePaper(package)
    return total

def calcualteTotalRibbonNeeded(dimensionList):
    total = 0
    for package in dimensionList:
        total+= calculateSinglePackageRibbon(package)
    return total

def createDimensionList(file):
    dimensions = []
    with open(file, "r") as f:
        for _ in f:
            d = _.strip().split("x")
            d = map(int, d)
            d = sorted(d)
            dimensions.append(tuple(d))
    return dimensions



print(calcualteTotalPaperNeeded(createDimensionList("dimensions.txt")))
print(calcualteTotalRibbonNeeded(createDimensionList("dimensions.txt")))