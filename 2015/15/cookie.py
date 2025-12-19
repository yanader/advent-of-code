from helpers import *
from ingredients import Ingredients

data = importFile("input.txt")

i = Ingredients()

for line in data:
    i.addIngredient(line)


recipe = {"Frosting": 40, "Candy": 20,"Butterscotch": 30, "Sugar": 10}
# recipe = {"Butterscotch": 44, "Cinnamon": 56}

print(i.totalScore(recipe))