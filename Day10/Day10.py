import os
import numpy as np

here = os.path.dirname(os.path.abspath(__file__))

input = r"PuzzleInput.txt"

filename = os.path.join(here, input)

class Solve():

    # Class constructor
    def __init__(self,part):
        self.ProgramCycle = 1
        self.ProgramValue = 1
        self.SignalStrength = 0
        self.ProgramResults = {}

        self.ReadInProgram()

        match part:
            case "Part 1":
                self.Part1()
            case "Part 2":
                self.Part2()

    # This function solves part 1 of the problem
    def Part1(self):
        self.runProgram()

        print("Signal strength: " + str(self.SignalStrength))

    # This function solves part 2 of the problem
    def Part2(self):
        self.runProgram()

        resultsString = ""

        for key in self.ProgramResults:
            pixelHorizontalPosition = (key - 1) % 40
            
            if abs(self.ProgramResults[key] - pixelHorizontalPosition) > 1:
                resultsString = "".join((resultsString, "."))
            else:
                resultsString = "".join((resultsString, "#"))

        for ii in range(6):
            print(resultsString[40*ii:40*ii+39])

    # This function runs the program from start to finish
    def runProgram(self):
        for commandIndex, command in enumerate(self.ProgramCommands):
            match command[0]:
                case "addx":
                    self.addx(command)
                case "noop":
                    self.noop()

    # This function parses the program rows from the input file
    def ReadInProgram(self):
        self.ProgramCommands = []

        with open(filename) as fp:
            rows = [p.strip() for p in fp.read().split('\n')]

        for row in rows:
            self.ProgramCommands.append(row.split())

    # This function executes the 'addx' command
    def addx(self, command):
        self.updateSignalStrength()
        self.storeProgramResults()
        self.ProgramCycle += 1
        
        self.updateSignalStrength()
        self.storeProgramResults()
        self.ProgramCycle += 1
        self.ProgramValue += int(command[1])
        
    # This function executes the 'noop' command
    def noop(self):
        self.updateSignalStrength()
        self.storeProgramResults()
        self.ProgramCycle += 1

    # This function stores the program cycle and value in a dictionary
    def storeProgramResults(self):
        self.ProgramResults[self.ProgramCycle] = self.ProgramValue

    # This function calculates the signal stength (if necessary)
    def updateSignalStrength(self):
        if self.ProgramCycle in [20, 60, 100, 140, 180, 220]:
            self.SignalStrength += self.ProgramCycle * self.ProgramValue

s = Solve("Part 2")
    

