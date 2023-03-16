import os
import numpy as np

here = os.path.dirname(os.path.abspath(__file__))

input = r"PuzzleInput.txt"

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
        d = DijkstrasAlgorithmPart1(self.heightMap, self.startPosition, self.endPosition)
        print("Length of shortest path: " + str(d.lengthOfShortestPath))

    # This function solves part 2 of the problem
    def Part2(self):
        d = DijkstrasAlgorithmPart2(self.heightMap, self.endPosition, 1)
        print("Length of shortest path: " + str(d.lengthOfShortestPath))

    # This function parses the required inputs from the input file
    def ReadInProgram(self):

        # Parse lines
        with open(filename) as fp:
            rows = [p.strip() for p in fp.read().split('\n')]

        # Split rows into individual elements
        self.heightMap = [[0]*len(rows[0]) for i in range(len(rows))]
        for rowIndex, row in enumerate(rows):
            for characterIndex, character in enumerate(row):

                # Find start and end positions
                if character == 'S':
                    self.startPosition = [rowIndex, characterIndex]
                    character = 'a'
                elif character == 'E':
                    self.endPosition = [rowIndex, characterIndex]
                    character = 'z'

                # Convert alphabetical height map to integer height map
                self.heightMap[rowIndex][characterIndex] = ord(character) - 96

class DijkstrasAlgorithmPart1():

    # Class constructor
    def __init__(self, heightMap, startNode, endNode):
        self.heightMap = heightMap
        self.startNode = startNode
        self.endNode = endNode

        self.initialise()
        self.findShortestPath()

    # This function initialises the algorithm
    def initialise(self):
        self.distance = [[0]*len(self.heightMap[0]) for i in range(len(self.heightMap))]
        self.analysedNodes = [[0]*len(self.heightMap[0]) for i in range(len(self.heightMap))]
        self.previousNode =[]

        for rowIndex, row in enumerate(self.heightMap):
            for elementIndex, element in enumerate(row):
                self.distance[rowIndex][elementIndex] = float('inf')
                self.analysedNodes[rowIndex][elementIndex] = 0
        
        self.distance[self.startNode[0]][self.startNode[1]] = 0

    # This function implements Dijkstra's path-finding algorithm
    def findShortestPath(self):
        while any(0 in row for row in self.analysedNodes):

            # Find unanalysed node with smallest distance
            minDistance = float('inf')
            for rowIndex, row in enumerate(self.distance):
                for elementIndex, element in enumerate(row):
                    if self.analysedNodes[rowIndex][elementIndex] == 0:
                        if minDistance > element:
                            minDistance = element
                            minDistanceRowIndex = rowIndex
                            minDistanceElementIndex = elementIndex

            # Mark selected node as analysed
            self.analysedNodes[minDistanceRowIndex][minDistanceElementIndex] = 1

            # Check if node being analysed is end node. If it is, break out of the loop
            if minDistanceRowIndex == self.endNode[0] and minDistanceElementIndex == self.endNode[1]:
                self.lengthOfShortestPath = self.distance[minDistanceRowIndex][minDistanceElementIndex]
                break

            # Find all unanalysed neighbours of node being analysed
            neighbours = findAllUnanalysedNeighboursOfNode(self.analysedNodes, [minDistanceRowIndex, minDistanceElementIndex])

            # For all valid neighbours
            for neighbour in neighbours:
                tempDistance = self.distance[minDistanceRowIndex][minDistanceElementIndex] + 1
                if self.heightMap[neighbour[0]][neighbour[1]] - self.heightMap[minDistanceRowIndex][minDistanceElementIndex] <= 1:
                    if tempDistance < self.distance[neighbour[0]][neighbour[1]]:
                        self.distance[neighbour[0]][neighbour[1]] = tempDistance
    
class DijkstrasAlgorithmPart2():

    # Class constructor
    def __init__(self, heightMap, startNode, endValue):
        self.heightMap = heightMap
        self.startNode = startNode
        self.endValue = endValue

        self.initialise()
        self.findShortestPath()

    # This function initialises the algorithm
    def initialise(self):
        self.distance = [[0]*len(self.heightMap[0]) for i in range(len(self.heightMap))]
        self.analysedNodes = [[0]*len(self.heightMap[0]) for i in range(len(self.heightMap))]
        self.previousNode =[]

        for rowIndex, row in enumerate(self.heightMap):
            for elementIndex, element in enumerate(row):
                self.distance[rowIndex][elementIndex] = float('inf')
                self.analysedNodes[rowIndex][elementIndex] = 0
        
        self.distance[self.startNode[0]][self.startNode[1]] = 0

    # This function implements Dijkstra's path-finding algorithm
    def findShortestPath(self):
        while any(0 in row for row in self.analysedNodes):

            # Find unanalysed node with smallest distance
            minDistance = float('inf')
            for rowIndex, row in enumerate(self.distance):
                for elementIndex, element in enumerate(row):
                    if self.analysedNodes[rowIndex][elementIndex] == 0:
                        if minDistance > element:
                            minDistance = element
                            minDistanceRowIndex = rowIndex
                            minDistanceElementIndex = elementIndex

            # Mark selected node as analysed
            self.analysedNodes[minDistanceRowIndex][minDistanceElementIndex] = 1

            # Check if node being analysed has value self.endValue. If it is, break out of the loop
            if self.heightMap[minDistanceRowIndex][minDistanceElementIndex] == self.endValue:
                self.lengthOfShortestPath = self.distance[minDistanceRowIndex][minDistanceElementIndex]
                break

            # Find all unanalysed neighbours of node being analysed
            neighbours = findAllUnanalysedNeighboursOfNode(self.analysedNodes, [minDistanceRowIndex, minDistanceElementIndex])

            # For all valid neighbours
            for neighbour in neighbours:
                tempDistance = self.distance[minDistanceRowIndex][minDistanceElementIndex] + 1
                if self.heightMap[minDistanceRowIndex][minDistanceElementIndex] - self.heightMap[neighbour[0]][neighbour[1]] <= 1:
                    if tempDistance < self.distance[neighbour[0]][neighbour[1]]:
                        self.distance[neighbour[0]][neighbour[1]] = tempDistance

# This function finds all of the unanalysed nodes for a given node
def findAllUnanalysedNeighboursOfNode(analysedNodes, nodePosition):

    # Function to check whether the neighbour is valid (ie. exits on the heightmap grid)
    def validNeighbour(neighbour):
        valid = True
        if neighbour[0] < 0 or neighbour[1] < 0:
            valid = False
        elif neighbour[0] >= len(analysedNodes) or neighbour[1] >= len(analysedNodes[0]):
            valid = False
        return valid
    
    possibleNeighbours = []
    possibleNeighbours.append([nodePosition[0] + 1, nodePosition[1]])
    possibleNeighbours.append([nodePosition[0] - 1, nodePosition[1]])
    possibleNeighbours.append([nodePosition[0], nodePosition[1] + 1])
    possibleNeighbours.append([nodePosition[0], nodePosition[1] - 1])


    neighbours = [neighbour for neighbour in possibleNeighbours if validNeighbour(neighbour)]

    return neighbours

s = Solve("Part 2")