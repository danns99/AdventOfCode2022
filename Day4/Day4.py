import os
import numpy as np

here = os.path.dirname(os.path.abspath(__file__))

input = r"PuzzleInput.txt"

filename = os.path.join(here, input)

with open(filename) as fp:
    pairList = [p.strip() for p in fp.read().split('\n')]

#Part I

numberOfFullyContained = 0
numberOfContained = 0

for pair in pairList:
    elves = pair.split(',')

    firstElf = elves[0]
    secondElf = elves[1]

    firstElfBounds = [int(x) for x in firstElf.split('-')]
    secondElfBounds = [int(x) for x in secondElf.split('-')]

    fullyContained = 0

    if firstElfBounds[0] != firstElfBounds[1] and secondElfBounds[0] != secondElfBounds[1]:
        if firstElfBounds[0] >= secondElfBounds[0] and firstElfBounds[1] <= secondElfBounds[1]:
            fullyContained = 1
        if firstElfBounds[0] <= secondElfBounds[0] and firstElfBounds[1] >= secondElfBounds[1]:
            fullyContained = 1

    if firstElfBounds[0] == firstElfBounds[1]:
        if firstElfBounds[0] >= secondElfBounds[0] and firstElfBounds[1] <= secondElfBounds[1]:
            fullyContained = 1
        
    if secondElfBounds[0] == secondElfBounds[1]:
        if secondElfBounds[0] >= firstElfBounds[0] and secondElfBounds[1] <= firstElfBounds[1]:
            fullyContained = 1
    
    if fullyContained == 1:
        numberOfFullyContained += 1

    #Part II
    contained = 0

    firstElfSections = np.linspace(int(firstElfBounds[0]),int(firstElfBounds[1]),(int(firstElfBounds[1]) - int(firstElfBounds[0])) + 1)
    secondElfSections = np.linspace(int(secondElfBounds[0]),int(secondElfBounds[1]),(int(secondElfBounds[1]) - int(secondElfBounds[0])) + 1)

    for section in firstElfSections:
        if section in secondElfSections:
            contained = 1

    for section in secondElfSections:
        if section in firstElfSections:
            contained = 1
    
    if contained == 1:
        numberOfContained += 1

print(numberOfFullyContained)
print(numberOfContained)