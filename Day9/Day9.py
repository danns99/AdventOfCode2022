import os
import numpy as np

here = os.path.dirname(os.path.abspath(__file__))

input = r"PuzzleInput.txt"

filename = os.path.join(here, input)

class Movements():
    def __init__(self, part):
        self.StartPosition = [0.0, 0.0]
        self.HeadPosition = self.StartPosition
        self.MovementList = []
        self.KnotPositionRecord = np.array([str(self.StartPosition[0]) + " " + str(self.StartPosition[1])])
        self.ReadInMovements()
        match part:
            case "Part 1":
                self.Part1()
            case "Part 2":
                self.Part2()

    def ReadInMovements(self):
        with open(filename) as fp:
            MovementRows = [p.strip() for p in fp.read().split('\n')]
        for row in MovementRows:
            self.MovementList.append(row)

    def Part1(self):
        TailPosition = self.StartPosition
        for row in self.MovementList:
            NumberOfMoves = int(row.split()[1])
            for i in range(1,NumberOfMoves+1):
                self.CalcHeadMovement(row)
                TailPosition = self.CalcKnotMovement(self.HeadPosition, TailPosition)
                self.StoreKnotPositions(TailPosition)
        self.CalcNumberOfKnotPositions()

    def Part2(self):
        NumberOfKnots = 10
        NumberOfTails = NumberOfKnots - 1
        KnotPositions = np.zeros(shape=(NumberOfTails, 2))
        KnotPositions[0][:] = self.StartPosition
        #self.PrintHeadTailPositions()
        for row in self.MovementList:
            NumberOfMoves = int(row.split()[1])
            for move in range(1, NumberOfMoves + 1):
                self.CalcHeadMovement(row)
                for knotIndex in range(0, NumberOfKnots - 1):
                    # Ensure the first knot follows the head
                    if knotIndex == 0:
                        KnotPositions[0][:] = self.CalcKnotMovement(self.HeadPosition, KnotPositions[0][:])
                    # Ensure the other knots follow the knots in front of them
                    else:
                        KnotPositions[knotIndex][:] = self.CalcKnotMovement(KnotPositions[knotIndex - 1][:], KnotPositions[knotIndex][:])
                self.StoreKnotPositions(KnotPositions[NumberOfTails - 1][:])
        self.CalcNumberOfKnotPositions()

    def CalcHeadMovement(self, row):
        MovementDirection = row[0]
        match MovementDirection:
            case "U":
                self.HeadPosition = [self.HeadPosition[0], self.HeadPosition[1] + 1]
            case "R":
                self.HeadPosition = [self.HeadPosition[0] + 1, self.HeadPosition[1]]
            case "L":
                self.HeadPosition = [self.HeadPosition[0] - 1, self.HeadPosition[1]]
            case "D":
                self.HeadPosition = [self.HeadPosition[0], self.HeadPosition[1] - 1]
            case _:
                print("Error: Invalid movement detected")

    def CalcKnotMovement(self, LeadingKnot, TrailingKnot):
        RelativePosition = [LeadingKnot[0] - TrailingKnot[0], LeadingKnot[1] - TrailingKnot[1]]

        TrailingKnotUpdated = TrailingKnot
        
        if abs(RelativePosition[0]) >= 2 or abs(RelativePosition[1]) >= 2:# or (abs(RelativePosition[0] == 1 and abs(RelativePosition[1] == 1))):
            if RelativePosition[0] == 0 and RelativePosition[1] > 0:                
                TrailingKnotUpdated = [TrailingKnot[0], TrailingKnot[1] + 1]
            elif RelativePosition[0] == 0 and RelativePosition[1] < 0:
                TrailingKnotUpdated = [TrailingKnot[0], TrailingKnot[1] - 1]
            elif RelativePosition[0] > 0 and RelativePosition[1] == 0:   
                TrailingKnotUpdated = [TrailingKnot[0] + 1, TrailingKnot[1]]
            elif RelativePosition[0] < 0 and RelativePosition[1] == 0:   
                TrailingKnotUpdated = [TrailingKnot[0] - 1, TrailingKnot[1]]
            elif RelativePosition[0] > 0 and RelativePosition[1] > 0:
                TrailingKnotUpdated = [TrailingKnot[0] + 1, TrailingKnot[1] + 1]
            elif RelativePosition[0] > 0 and RelativePosition[1] < 0:
                TrailingKnotUpdated = [TrailingKnot[0] + 1, TrailingKnot[1] - 1]
            elif RelativePosition[0] < 0 and RelativePosition[1] > 0:
                TrailingKnotUpdated = [TrailingKnot[0] - 1, TrailingKnot[1] + 1]
            elif RelativePosition[0] < 0 and RelativePosition[1] < 0:
                TrailingKnotUpdated = [TrailingKnot[0] - 1, TrailingKnot[1] - 1]

        return TrailingKnotUpdated

    def StoreKnotPositions(self, Knot):
        self.KnotPositionRecord = np.append(self.KnotPositionRecord, [str(Knot[0]) + " " + str(Knot[1])])

    def CalcNumberOfKnotPositions(self):
        self.NumberOfUniqueKnotPositions = len(np.unique(self.KnotPositionRecord))
        print("Answer: ",self.NumberOfUniqueKnotPositions)

m = Movements("Part 2")