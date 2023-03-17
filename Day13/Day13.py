import os
from copy import deepcopy

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
        indices = []

        for packetIndex in range(0, len(self.leftPackets)):

            comparison = self.compare_lists(self.leftPackets[packetIndex], self.rightPackets[packetIndex])

            if comparison == 1:
                indices.append(packetIndex + 1)
        
        print(sum(indices))
        
    # This function solves part 2 of the problem
    def Part2(self):
        packets = []

        for packetIndex in range(len(self.leftPackets)):
            packets.append(self.leftPackets[packetIndex])
            packets.append(self.rightPackets[packetIndex])

        packets.append([[2]])
        packets.append([[6]])

        sortedPackets = self.bubbleSort(packets)

        decoderKey = (sortedPackets.index([[2]]) + 1) * (sortedPackets.index([[6]]) + 1)
        print(decoderKey)

    # This function compares two supplied inputs as per the rules of the challenge
    def compare_lists(self, first, second):

        while len(first) > 0 and len(second) > 0:
            left = first.pop(0)
            right = second.pop(0)
            
            if type(left) == int and type(right) == int:
                if left < right:
                    return 1
                elif left > right:
                    return -1
            if type(left) == list and type(right) == list:
                sub_comparison = self.compare_lists(left, right)
                if sub_comparison != 0:
                    return sub_comparison
            if type(left) == int and type(right) == list:
                sub_comparison = self.compare_lists(list([left]), right)
                if sub_comparison != 0:
                    return sub_comparison
            if type(left) == list and type(right) == int:
                sub_comparison = self.compare_lists(left, list([right]))
                if sub_comparison != 0:
                    return sub_comparison

        if len(first) < len(second):
            return 1
        elif len(first) > len(second):
            return -1
        else:
            return 0
    
    # This function sorts a list of elements using a bubble sort algorithm
    def bubbleSort(self, packets):

        for ii in range(len(packets)):
            for jj in range(0, len(packets) - ii - 1):
                if self.compare_lists(deepcopy(packets[jj]), deepcopy(packets[jj + 1])) == -1:
                    packets[jj], packets[jj + 1] = packets[jj + 1], packets[jj]
        
        return packets

    # This function parses the required inputs from the input file
    def ReadInProgram(self):

        # Parse lines
        with open(filename) as fp:
            rows = [p.strip() for p in fp.read().split('\n')]

        self.leftPackets = []
        self.rightPackets = []

        # Sort packets into leftPackets and rightPackets
        for ii in range(0, len(rows) - 1, 3):
            self.leftPackets.append(eval(rows[ii]))
            self.rightPackets.append(eval(rows[ii + 1]))

s = Solve("Part 2")