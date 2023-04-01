import os

here = os.path.dirname(os.path.abspath(__file__))

input = r"PuzzleInput.txt"

filename = os.path.join(here, input)

class Solve():

    # Class constructor
    def __init__(self,part):

        self.ReadInProgram()
        self.calculateRockPositions()

        match part:
            case "Part 1":
                self.Part1()
            case "Part 2":
                self.Part2()

    # This function solves part 1 of the problem
    def Part1(self):
        self.sandRestingPositions = []

        self.sandInAbyssVar = False
        # Stop simulation when sand starts falling into abyss
        while not self.sandInAbyssVar:
            self.simSandMotion()

        print(len(self.sandRestingPositions))        
        
    # This function solves part 2 of the problem
    def Part2(self):
        self.sandRestingPositions = []

        self.addRockFloor()

        while True:
            self.simSandMotion()
            # Stop simulation when sand is at starting point
            if self.sandRestingPositions[len(self.sandRestingPositions) - 1] == [500, 0]:
                break

        print(len(self.sandRestingPositions)) 

    # This function parses the required inputs from the input file
    def ReadInProgram(self):

        # Parse lines
        with open(filename) as fp:
            rockNodes = [p.strip() for p in fp.read().split('\n')]

        self.rockNodes = []
        for rockNode in rockNodes:
            splitRow = [[int(node) for node in row] for row in [node.split(',') for node in rockNode.split(' -> ')]]
            self.rockNodes.append(splitRow)

    # This function calculates a list of rock positions from the parsed rock nodes
    def calculateRockPositions(self):
        self.rockPositions = []

        for rockNodes in self.rockNodes:
            for ii in range(0, len(rockNodes) - 1):
                # If true then rock path is vertical. If false then rock path is horizontal.
                if rockNodes[ii][0] == rockNodes[ii+1][0]:
                    distanceToNextNode = rockNodes[ii][1] - rockNodes[ii+1][1]

                    if distanceToNextNode < 0:
                        step = 1
                    else:
                        step = -1

                    rockDistances = [*range(rockNodes[ii][1], rockNodes[ii+1][1], step)]

                    for distance in rockDistances:
                        self.rockPositions.append([rockNodes[ii][0], distance])
                else:
                    distanceToNextNode = rockNodes[ii][0] - rockNodes[ii+1][0]

                    if distanceToNextNode < 0:
                        step = 1
                    else:
                        step = -1

                    rockDistances = [*range(rockNodes[ii][0], rockNodes[ii+1][0], step)]

                    for distance in rockDistances:
                        self.rockPositions.append([distance, rockNodes[ii][1]])

            self.rockPositions.append(rockNodes[len(rockNodes) - 1])

    # This function simulates the motion of the sand falling through the cave
    def simSandMotion(self):
        sandPosition = [500, 0]
        motionPossible = True
        while motionPossible:
            possiblePositions = [[sandPosition[0], sandPosition[1] + 1], [sandPosition[0] - 1, sandPosition[1] + 1], [sandPosition[0] + 1, sandPosition[1] + 1]]
            for possiblePosition in possiblePositions:
                if (possiblePosition not in self.rockPositions) and (possiblePosition not in self.sandRestingPositions):
                    sandPosition = possiblePosition
                    break
                motionPossible = self.isMotionPossible(sandPosition)
            
            if self.sandInAbyss(sandPosition):
                self.sandInAbyssVar = True
                break

        if not self.sandInAbyss(sandPosition):
            self.sandRestingPositions.append(sandPosition)

    # This function calculates whether motion is possible for a grain of sand in a given position
    def isMotionPossible(self, sandPosition):
        possiblePositions = [[sandPosition[0] - 1, sandPosition[1] + 1], [sandPosition[0], sandPosition[1] + 1], [sandPosition[0] + 1, sandPosition[1] + 1]]

        motionPossible = False
        for possiblePosition in possiblePositions:
            if possiblePosition not in self.rockPositions and possiblePosition not in self.sandRestingPositions:
                motionPossible = True

        return motionPossible
    
    # This function calculates whether sand has fallen into the abyss
    def sandInAbyss(self, sandPosition):
        sandInAbyss = False
        heights = [rockPosition[1] for rockPosition in self.rockPositions]
        if (sandPosition[1] > max(heights)):
            sandInAbyss = True

        return sandInAbyss
    
    # This function adds the rock floor required for part 2 of the problem
    def addRockFloor(self):
        heights = [rockPosition[1] for rockPosition in self.rockPositions]
        heightFromSourceToFloor = max(heights) + 2

        # Only need to add floor +/- heightFromSourceToFloor + 1 x-coordinate
        for x in range(500 - (heightFromSourceToFloor + 1), 500 + (heightFromSourceToFloor + 1)):
            self.rockPositions.append([x, heightFromSourceToFloor])


s = Solve("Part 1")

    