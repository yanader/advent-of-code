from helpers import *
from ingredients import Ingredients

data = importFile("input.txt")

ing = Ingredients()

for line in data:
    ing.addIngredient(line)


# recipe = {"Frosting": 40, "Candy": 20,"Butterscotch": 30, "Sugar": 10}
# recipe = {"Butterscotch": 44, "Cinnamon": 56}

maxScore = 0

# print(ing.totalScore(recipe))

for i in range(101):
    for j in range(101):
        for k in range(101):
            for l in range(101):
                teaspoons = {"Frosting": i, "Candy": j,"Butterscotch": k, "Sugar": l}
                if i + j + k + l != 100:
                    continue
                if ing.calculateCalories(teaspoons) != 500:
                    continue
                newScore = ing.totalScore(teaspoons)
                if newScore > maxScore:
                    maxScore = newScore

print(maxScore)