import os
import networkx

here = os.path.dirname(os.path.abspath(__file__))

input = "PuzzleInput.txt"

filename = os.path.join(here, input)

class Solve():

    # Class constructor
    def __init__(self,part):

        self.ReadInProgram()
        
        self.calculateShortestDistances()

        match part:
            case "Part 1":
                self.Part1()
            case "Part 2":
                self.Part2()

    # This function solves part 1 of the problem
    def Part1(self):
        print("Answer to Part 1: " + str(max(self.visit('AA', 30, 0, 0, {}).values())))

    def Part2(self):
        visited2 = self.visit('AA', 26, 0, 0, {})
        print("Answer to part 2: " + str(max(v1+v2 for bitm1, v1 in visited2.items() for bitm2, v2 in visited2.items() if not bitm1 & bitm2)))

    # This function parses the required information from the input
    def ReadInProgram(self):

        self.valveDict = {}
        self.G = networkx.Graph()

         # Parse lines
        with open(filename) as fp:
            valves = [p.strip() for p in fp.read().split('\n')]

        # Parse information for each valve and store in valve object
        for i, valve in enumerate(valves):
            valveCode = valve.split(' has flow rate=')[0].split('Valve ')[1]
            valveFlowRate = int(valve.split(' has flow rate=')[1].split('; tunnel')[0])
            valveConnections = valve.split(' has flow rate=')[1].split('to valve')[1].replace('s','').replace(' ','').split(',')
            valveIndex = 1 << i

            for connection in valveConnections:
                self.G.add_edge(valveCode, connection)
                self.G.add_edge(connection, valveCode)

            # Append to the dictionary to store all valve flow rates, connections and indices
            self.valveDict[valveCode] = Valve(valveFlowRate, valveConnections, valveIndex)

        # Create a dictionary for all of the pipes with a non-zero flow rate
        self.pipesWithNonZeroFlowRate = {valve: self.valveDict[valve].flowRate for valve in self.valveDict if self.valveDict[valve].flowRate != 0}

    # This function is to calculate the shortest distance between any possible pair of valves
    def calculateShortestDistances(self):

        # Create dictionary to store shortest distances
        self.shortestDistances = {}

        # Iterate for each pair of valves
        for valve1 in self.valveDict:
            for valve2 in self.valveDict:
                self.shortestDistances[(valve1,valve2)] = len(networkx.shortest_path(self.G, valve1, valve2)) - 1

    def visit(self, valve, minutes, bitmask, pressure, answer):
        answer[bitmask] = max(answer.get(bitmask, 0), pressure)
        
        # Only loop over valves which have a non-zero flow rate
        for valve2, flow in self.pipesWithNonZeroFlowRate.items():
            remaining_minutes = minutes - self.shortestDistances[valve, valve2] - 1
            if self.valveDict[valve2].valveIndex & bitmask or remaining_minutes <= 0: continue
            self.visit(valve2, remaining_minutes, bitmask|self.valveDict[valve2].valveIndex, pressure + flow * remaining_minutes, answer)
        return answer

# This is a class to represent each valve
class Valve():

    # Class constructor
    def __init__(self, flowRate, valveConnections, valveIndex):
        self.flowRate = flowRate
        self.valveConnections = valveConnections
        self.valveIndex = valveIndex


s = Solve("Part 2")