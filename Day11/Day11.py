import os
import numpy as np
import math

here = os.path.dirname(os.path.abspath(__file__))

input = r"PuzzleInput.txt"

filename = os.path.join(here, input)

Monkeys = []

class Solve():

    # Class constructor
    def __init__(self,part):

        self.ReadInProgram()

        match part:
            case "Part 1":
                self.Part1()
            case "Part 2":
                self.Part2()

    # This function solves part 1 of the problem
    def Part1(self):
        numberOfRounds = 20
        self.simulate(numberOfRounds, 1, 0)

    # This function solves part 2 of the problem
    def Part2(self):
        superMod = 1
        for divisors in [m.testDivisor for m in Monkeys]:
            superMod *= int(divisors)

        numberOfRounds = 10000
        self.simulate(numberOfRounds, 2, superMod)

    # This function simulates the monkeys sorting the items
    def simulate(self, numberOfRounds, part, superMod):
        for round in range(numberOfRounds):
            for monkey in Monkeys:
                monkey.completeTurn(part, superMod)

        inspectionCounts = []

        for monkey in Monkeys:
            inspectionCounts.append(monkey.inspectionCount)

        highestInspectionCount = max(inspectionCounts)
        inspectionCounts.remove(highestInspectionCount)
        secondHighestInspectionCount = max(inspectionCounts)

        print("Level of monkey business: " + str(highestInspectionCount * secondHighestInspectionCount))

    # This function parses the required inputs from the input file
    def ReadInProgram(self):

        # Parse lines
        with open(filename) as fp:
            rows = [p.strip() for p in fp.read().split('\n')]

        # Split lines into words
        rowsSplit = []
        for row in rows:
            rowsSplit.append(row.split())

        # Parse required inputs for each monkey
        for rowSplitIndex, rowSplit in enumerate(rowsSplit):
            if len(rowSplit) != 0:
                if rowSplit[0] == 'Monkey':
                    monkeyNumber = rowSplit[1][0]
                    startingItems = rowsSplit[rowSplitIndex + 1][2 : None]
                    startingItems = [item.replace(',', '') for item in startingItems]
                    operationOperator = rowsSplit[rowSplitIndex + 2][4]
                    operationNumber = rowsSplit[rowSplitIndex + 2][5]
                    testDivisor = rowsSplit[rowSplitIndex + 3][3]
                    trueMonkey = rowsSplit[rowSplitIndex + 4][5]
                    falseMonkey = rowsSplit[rowSplitIndex + 5][5]

                    monkey = Monkey(monkeyNumber, startingItems, operationOperator, operationNumber, testDivisor, trueMonkey, falseMonkey)
                    Monkeys.append(monkey)

class Monkey():

    # Class constructor
    def __init__(self, monkeyNumber, starting_items, operationOperator, operationNumber , testDivisor, trueMonkey, falseMonkey):
        self.monkeyNumber = monkeyNumber
        self.items = starting_items
        self.operationOperator = operationOperator
        self.operationNumber = operationNumber
        self.testDivisor = testDivisor
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
        self.inspectionCount = 0
    
    # This function completes a single monkeys turn
    def completeTurn(self, part, superMod):
        if len(self.items) != 0:
            match part:
                case 1:
                    self.performOperationsPart1()
                case 2:
                    self.performOperationsPart2(superMod)
            self.discardItems()

    # This function performs the monkey operations (part 1)
    def performOperationsPart1(self):
        for itemIndex, item in enumerate(self.items):
            # Perform operation
            match self.operationOperator:
                case "+":
                    if self.operationNumber == "old":
                        output = int(self.items[itemIndex]) + int(self.items[itemIndex])
                    else:
                        output = int(self.items[itemIndex]) + int(self.operationNumber)
                case "*":
                    if self.operationNumber == "old":
                        output = int(self.items[itemIndex]) ** 2
                    else:
                        output = int(self.items[itemIndex]) * int(self.operationNumber)

            # Perform post operation operation
            output = math.floor(output / 3)
            self.items[itemIndex] = output

            self.inspectionCount += 1

    # This function performs the monkey operations (part 2)
    def performOperationsPart2(self, superMod):
        for itemIndex, item in enumerate(self.items):
            # Perform operation
            match self.operationOperator:
                case "+":
                    if self.operationNumber == "old":
                        output = int(self.items[itemIndex]) + int(self.items[itemIndex])
                    else:
                        output = int(self.items[itemIndex]) + int(self.operationNumber)
                case "*":
                    if self.operationNumber == "old":
                        output = int(self.items[itemIndex]) ** 2
                    else:
                        output = int(self.items[itemIndex]) * int(self.operationNumber)

            # Perform post operation operation
            output = output % superMod
            self.items[itemIndex] = output

            self.inspectionCount += 1
    
    # This function tests the worry level and discards the item to the correct monkey
    def discardItems(self):        
        for item in self.items[:]:
            if (int(item) % int(self.testDivisor)) == 0:
                self.throwItem(Monkeys[int(self.trueMonkey)], 0)
            else:
                self.throwItem(Monkeys[int(self.falseMonkey)], 0)

    # This function transfers an item from one monkey to another
    def throwItem(self, monkey, itemIndex):
        monkey.items.append(self.items[itemIndex])
        self.items.pop(itemIndex)

s = Solve("Part 2")
    

