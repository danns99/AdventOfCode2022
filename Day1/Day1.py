# Part I
import os

here = os.path.dirname(os.path.abspath(__file__))

input = r"PuzzleInput.txt"

filename = os.path.join(here, input)

with open(filename) as fp:
    elvesList = [p.strip() for p in fp.read().split('\n\n')]

caloriesSum = []

for elves in elvesList:
    caloriesList = elves.split('\n')
    totalCalories = sum(list(map(int, caloriesList)))
    caloriesSum.append(totalCalories)

maxCalories = max(caloriesSum)

# Part II
maxCalories1 = max(caloriesSum)
caloriesSum.remove(maxCalories1)

maxCalories2 = max(caloriesSum)
caloriesSum.remove(maxCalories2)

maxCalories3 = max(caloriesSum)
caloriesSum.remove(maxCalories3)

sumMaxCalories123 = maxCalories1 + maxCalories2 + maxCalories3

print (sumMaxCalories123)