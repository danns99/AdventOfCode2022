import os

here = os.path.dirname(os.path.abspath(__file__))

input = "PuzzleInput.txt"

filename = os.path.join(here, input)

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
        # Define constants
        numberOfSimulations = 2022
        self.tunnelWidth = 7
        self.jetBlastIndex = 0

        # Simulate rockfall
        self.simulate(numberOfSimulations)

        print("Answer to Part 1: " + str(self.calcHighestPoint() + 1))

    # This function solves part 2 of the problem
    def Part2(self):
        
        # Solution not yet implemented
        pass

    # This function parses the required information from the input
    def ReadInProgram(self):

         # Parse input
        self.jetPattern = list(open(filename).read())

    # This function simulates the rockfall through the cave
    def simulate(self, numberOfSimulations):

        # Start by defining the tunnel as having height 10 (arbitrary). This will increase as blocks start to fall
        # The 0th element in self.tunnel represents the bottom row, the 1st element represents the 2nd row, etc.
        self.tunnel = [[0] * self.tunnelWidth for i in range(10)]

        # Loop for the desired number of rocks
        for i in range(numberOfSimulations):

            # Obtain rock shape
            rockShape = i % 5

            # Calculate highest rock in tunnel
            highestPoint = self.calcHighestPoint()

            # Ensure self.tunnel has enough rows
            if (len(self.tunnel) < highestPoint + 10):

                # Add 10 rows to self.tunnel (arbitrary)
                for i in range(10):
                    self.tunnel.append([0,0,0,0,0,0,0])

            # Simulate motion of single rock
            self.simulateSingleRock(rockShape, highestPoint)

    # This function calculates the current direction of the jet blast
    def calculateJetBlastDirection(self) -> str:

        # Obtain direction of jet blast
        jetDirection = self.jetPattern[self.jetBlastIndex % len(self.jetPattern)]

        self.jetBlastIndex += 1

        return jetDirection
        

    # This function is to calculate the row of the highest rock in the tunnel
    def calcHighestPoint(self) -> int:
        for rowNumber, row in enumerate(self.tunnel):
            if 1 not in row:
                return rowNumber - 1
        
        # This will only be reached if no rocks have fallen, meaning the highest point is the floor
        return -1

    # This function is to simulate the motion of a single rock through the tunnel
    def simulateSingleRock(self, rockShape, highestPoint):

        # Calculate starting point of rock (left edge 2 units from left wall and bottom edge 3 units above highest rock in tunnel)
        initalRockDatum = [2, highestPoint + 4]

        # Initialise rock object
        rock = Rock(rockShape, initalRockDatum)

        # Loop until break is called
        while 1:

            # Obtain jet direction
            jetDirection = self.calculateJetBlastDirection()

            # Blow rock with jet
            newCoords = rock.moveRock(jetDirection, self.tunnel)

            # Update rocks coordinates
            rock.updateRockCoordinates(newCoords)

            # Make rock fall 1 unit
            newCoords = rock.moveRockDown()

            # Check if rock is settled
            if (rock.checkIfRockSettled(self.tunnel, newCoords)):
                break
            
            # Update rocks coordinates
            rock.updateRockCoordinates(newCoords)

        # Add rocks resting position to tunnel map
        for coord in rock.rockCoords:
            self.tunnel[coord[1]][coord[0]] = 1

# Class to represent a rock object
class Rock():

    # Class constructor
    def __init__(self, rockType, initalRockDatum):
        self.rockType = rockType

        # Using rock type, define rock coordinates
        self.defineInitialRockCoords(initalRockDatum)

    # Function to define the inital co-ordinates of the rock. The bottom left corner of the rock is defined as [0,0] (relative), with
    # postive x and y representing leftwards and upwards respectively
    def defineInitialRockCoords(self, initalRockDatum):
        self.rockCoords = []

        # Define rock shape
        match self.rockType:
            # ####
            case 0:
                self.rockCoords.append([0+initalRockDatum[0],0+initalRockDatum[1]])
                self.rockCoords.append([1+initalRockDatum[0],0+initalRockDatum[1]])
                self.rockCoords.append([2+initalRockDatum[0],0+initalRockDatum[1]])
                self.rockCoords.append([3+initalRockDatum[0],0+initalRockDatum[1]])

            # .#.
            # ###
            # .#.           
            case 1:
                self.rockCoords.append([1+initalRockDatum[0],0+initalRockDatum[1]])
                self.rockCoords.append([0+initalRockDatum[0],1+initalRockDatum[1]])
                self.rockCoords.append([1+initalRockDatum[0],1+initalRockDatum[1]])
                self.rockCoords.append([1+initalRockDatum[0],2+initalRockDatum[1]])
                self.rockCoords.append([2+initalRockDatum[0],1+initalRockDatum[1]])

            # ..#
            # ..#
            # ###
            case 2:
                self.rockCoords.append([0+initalRockDatum[0],0+initalRockDatum[1]])
                self.rockCoords.append([1+initalRockDatum[0],0+initalRockDatum[1]])
                self.rockCoords.append([2+initalRockDatum[0],0+initalRockDatum[1]])
                self.rockCoords.append([2+initalRockDatum[0],1+initalRockDatum[1]])
                self.rockCoords.append([2+initalRockDatum[0],2+initalRockDatum[1]])

            # #
            # #
            # #
            # #
            case 3:
                self.rockCoords.append([0+initalRockDatum[0],0+initalRockDatum[1]])
                self.rockCoords.append([0+initalRockDatum[0],1+initalRockDatum[1]])
                self.rockCoords.append([0+initalRockDatum[0],2+initalRockDatum[1]])
                self.rockCoords.append([0+initalRockDatum[0],3+initalRockDatum[1]])

            # ##
            # ##
            case 4:
                self.rockCoords.append([0+initalRockDatum[0],0+initalRockDatum[1]])
                self.rockCoords.append([0+initalRockDatum[0],1+initalRockDatum[1]])
                self.rockCoords.append([1+initalRockDatum[0],0+initalRockDatum[1]])
                self.rockCoords.append([1+initalRockDatum[0],1+initalRockDatum[1]])

    # This function is to simulate a movement on the rock object, of type '<', '>', and return the new coordinates
    def moveRock(self, movementType, tunnel) -> list[list[int]]:

        # Define movement dependant on movement type
        match movementType:
            case '<':
                newCoords = [[coord[0] - 1, coord[1]] for coord in self.rockCoords]
            case '>':
                newCoords = [[coord[0] + 1, coord[1]] for coord in self.rockCoords]

        # If movement would have caused rock to hit side of tunnel or other rock, return original coordinates
        for coord in newCoords:
            if coord[0] < 0 or coord[0] >= 7 or tunnel[coord[1]][coord[0]] == 1:
                return self.rockCoords

        # Only reached if side of tunnel
        return newCoords
    
    # This function is to simulate a downwards movement on the rock object, and return the new coordinates
    def moveRockDown(self) -> list[list[int]]:
        return [[coord[0], coord[1] - 1] for coord in self.rockCoords]

    # Function to update the co-ordinates of the rock
    def updateRockCoordinates(self, newCoords):
        self.rockCoords = newCoords

    # Function to check the validity of a rocks new co-ordinates
    def checkIfRockSettled(self, tunnel, newCoords) -> bool: 
        for coord in newCoords:
            if tunnel[coord[1]][coord[0]] == 1 or coord[1] == -1:
                return True
            
        # Only reached if rock hasn't settled
        return False
    
s = Solve("Part 1")