import re

class Ingredients:
    def __init__(self):
        self.ingredients = {}

    def addIngredient(self, line):
        parts = re.split(r'[ ,]', line)
        self.ingredients[parts[0][0:-1]] = {"capacity":int(parts[2]),"durability":int(parts[5]),"flavor":int(parts[8]),"texture":int(parts[11]),"calories":int(parts[14])}
    
    def totalScore(self, teaspoons):
        return (self.calculateCapacity(teaspoons) 
                * self.calculateDurability(teaspoons)
                * self.calculateFlavor(teaspoons)
                * self.calculateTexture(teaspoons))

    def calculateCapacity(self, teaspoons):
        score = 0
        for name, ingredient in self.ingredients.items():
            score += ingredient["capacity"] * teaspoons[name]
        return max(0, score)
    
    def calculateDurability(self, teaspoons):
        score = 0
        for name, ingredient in self.ingredients.items():
            score += ingredient["durability"] * teaspoons[name]
        return max(0, score)

    def calculateFlavor(self, teaspoons):
        score = 0
        for name, ingredient in self.ingredients.items():
            score += ingredient["flavor"] * teaspoons[name]
        return max(0, score)

    def calculateTexture(self, teaspoons):
        score = 0
        for name, ingredient in self.ingredients.items():
            score += ingredient["texture"] * teaspoons[name]
        return max(0, score)

    def calculateCalories(self, teaspoons):
        score = 0
        for name, ingredient in self.ingredients.items():
            score += ingredient["calories"] * teaspoons[name]
        return max(0, score)


    
    