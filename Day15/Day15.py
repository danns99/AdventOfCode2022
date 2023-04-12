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

        # Specify the row number to be analysed
        desiredRowNumber = 2000000

        # For the desired row number, find the bounds of where beacons cannot be located
        stripBoundsCompressed = self.findCompressedIntervalsForRow(desiredRowNumber)

        # Find the number of beacons or sensors located in the desired row
        beaconSensorCount = self.calculateNumberOfSensorsOrBeaconsInRow(desiredRowNumber)

        # Calculate the number of places the distress beacon cannot be located
        coverage_count = sum(bound[1]-bound[0]+1 for bound in stripBoundsCompressed)

        print("Answer to part 1: " + str(coverage_count - beaconSensorCount))

    def Part2(self):

        # Specify constants for the problem
        DISTRESS_BEACON_X_BOUNDS = [0, 4000000]
        DISTRESS_BEACON_Y_BOUNDS = [0, 4000000]
        self.TUNING_FREQ_MULTIPLIER = 4000000

        pointFound = False
        for sensor in self.sensors:

            # Calculate distance from sensor to beacon
            sensorToBeaconDistance = self.calculateManhattanDistance(sensor[0], sensor[1])

            for dx in range(sensorToBeaconDistance + 2):
                dy = (sensorToBeaconDistance + 1) - dx
                
                for sign_x, sign_y in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    x = sensor[0][0] + (dx * sign_x)
                    y = sensor[0][1] + (dy * sign_y)
                    
                    # Check within the bounds defined; if not, try next dx and dy
                    if not (DISTRESS_BEACON_X_BOUNDS[0] <= x <= DISTRESS_BEACON_X_BOUNDS[1]
                            and DISTRESS_BEACON_Y_BOUNDS[0] <= y <= DISTRESS_BEACON_Y_BOUNDS[1]):
                        continue

                    coverage = self.findCompressedIntervalsForRow(y)
                    if len(coverage) > 1:
                        for i in range(0, len(coverage)):
                            if coverage[i][0] > coverage[0][1] + 1:
                                x = coverage[i][0] - 1
                                distressCoordinate = [x, y]
                                pointFound = True
                                break
                    
                    if pointFound:
                        break
            if pointFound:
                break

        # Calculate tuning frequency from coordinates of distress beacon
        tuningFreq = self.calculateTuningFrequency(distressCoordinate)

        print("Answer to part 2: " + str(tuningFreq))

    # This function finds the bounds of where the distress beacon cannot be located for a given row number
    def findCompressedIntervalsForRow(self, rowNumber):

        stripBounds = []
        for sensor in self.sensors:
            # Calculate distance from sensor to beacon
            sensorToBeaconDistance = self.calculateManhattanDistance(sensor[0], sensor[1])

            if rowNumber in range(sensor[0][1] - sensorToBeaconDistance, sensor[0][1] + sensorToBeaconDistance):
                # Calculate half-width of strip in desired row that has a lower Manhattan distance from the sensor than the beacon
                stripHalfWidth = sensorToBeaconDistance - abs(sensor[0][1] - rowNumber)

                # Use strip half width to calculate strip bounds
                stripBounds.append([sensor[0][0] - stripHalfWidth, sensor[0][0] + stripHalfWidth])

        return self.compressIntervals(stripBounds)
    
    # This function calculates the number of sensors and beacons in a given row
    def calculateNumberOfSensorsOrBeaconsInRow(self, rowNumber):

        beaconSensorCount = 0
        countedBeacons = []
        for sensor in self.sensors:
            for item in sensor:
                        if item[1] == rowNumber and item not in countedBeacons:
                            # Count how many sensors/beacons are present in the target row
                            beaconSensorCount += 1

                            # Record that this beacon/sensor has been counted
                            countedBeacons.append(item)

        return beaconSensorCount

    # This function compresses a set of intervals such that there are no overlaps
    def compressIntervals(self, intervals):

        intervals.sort()
        stack = []
        stack.append(intervals[0])
        
        for interval in intervals[1:]:
            # Check for overlapping interval
            if stack[-1][0] <= interval[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], interval[-1])
            else:
                stack.append(interval)
         
        return stack

    # This function parses the required inputs from the input file
    def ReadInProgram(self):

        # Parse lines
        with open(filename) as fp:
            sensors = [p.strip() for p in fp.read().split('\n')]

        self.sensors = []
        for sensor in sensors:
            splitSensor = sensor.split(': closest beacon is at x=')
            sensorPos = [int(string) for string in splitSensor[0][12:len(splitSensor[0])].split(', y=')]
            beaconPos = [int(string) for string in splitSensor[1].split(', y=')]
            self.sensors.append([sensorPos, beaconPos])
    
    # This function calculates the Manhattan distance between two points
    def calculateManhattanDistance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    
    # This function calculates the tuning frequency for a coordinate
    def calculateTuningFrequency(self, coordinate):
        return coordinate[0] * self.TUNING_FREQ_MULTIPLIER + coordinate[1]

s = Solve("Part 2")    