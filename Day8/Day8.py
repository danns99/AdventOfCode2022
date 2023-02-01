def CalcViewingDistance(array, TreeHeightData):
    ViewingDistance = 0
    for ii in range(0, len(array), 1):
        ViewingDistance += 1
        if array[ii] >= TreeHeightData[i][j]:
            break
    return ViewingDistance

import os
import numpy as np

here = os.path.dirname(os.path.abspath(__file__))

input = r"PuzzleInput.txt"

filename = os.path.join(here, input)

with open(filename) as fp:
    TreeRows = [p.strip() for p in fp.read().split('\n')]   

# Calculate number of columns and rows of trees
NumberOfRows = len(TreeRows)
NumberOfColumns = len(TreeRows[0])

# Initialise a matrix to store tree height values. Set initial value to 0
TreeHeightData = np.empty(shape=(NumberOfRows,NumberOfColumns))
TreeHeightData.fill(0)

# Populate matrix with tree height data
for i in range(0, NumberOfRows, 1):

    rowString = list(map(int,TreeRows[i]))

    for j in range(0, NumberOfColumns, 1):

        TreeHeightData[i][j] = rowString[j]

# Iterate through all non-border trees to work out if they are visible
InnerVisibilityCounter = 0
MaxViewingDistance = 0

for i in range(1, NumberOfRows-1, 1):

    for j in range(1, NumberOfColumns-1, 1):

        TreeHeightDataRow = TreeHeightData[i,:]
        TreeHeightDataColumn = TreeHeightData[:,j]

        TreesAboveArray = TreeHeightDataColumn[0:i]
        TreesBelowArray = TreeHeightDataColumn[i+1:len(TreeHeightDataColumn)]

        TreesLeftArray = TreeHeightDataRow[0:j]
        TreesRightArray = TreeHeightDataRow[j+1:len(TreeHeightDataRow)]

        # Part I
        if (TreeHeightData[i][j] > max(TreesAboveArray)) | (TreeHeightData[i][j] > max(TreesBelowArray)) | (TreeHeightData[i][j] > max(TreesLeftArray)) | (TreeHeightData[i][j] > max(TreesRightArray)):
            InnerVisibilityCounter += 1

        #Part II
        # Invert TreesAboveArray and TreesLeftArray, such that increasing array index corresponds to increased distance from tree
        TreesAboveArray = np.flip(TreesAboveArray)
        TreesLeftArray = np.flip(TreesLeftArray)

        # Calculate viewing distances
        AboveViewingDistance = CalcViewingDistance(TreesAboveArray, TreeHeightData) 
        BelowViewingDistance = CalcViewingDistance(TreesBelowArray, TreeHeightData)
        LeftViewingDistance = CalcViewingDistance(TreesLeftArray, TreeHeightData)
        RightViewingDistance = CalcViewingDistance(TreesRightArray, TreeHeightData)

        # Calculate total viewing distance
        TotalViewingDistance = AboveViewingDistance * BelowViewingDistance * LeftViewingDistance * RightViewingDistance

        # Check if total viewing distance is greater than existing maximum
        MaxViewingDistance = max(TotalViewingDistance, MaxViewingDistance)

# Calculate how many outer trees there are
OuterTreeCount = 2 * (NumberOfColumns + NumberOfRows - 2)

# Calculate total number of visible trees
TotalVisibleTreeCount = InnerVisibilityCounter + OuterTreeCount

# Part I
print("Answer to part 1: ", TotalVisibleTreeCount)

# Part II
print("Answer to part 2: ", MaxViewingDistance)