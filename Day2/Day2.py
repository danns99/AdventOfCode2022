# Part I
def CalculateRoundScore1(oppositionPlay, playerPlay):
    if oppositionPlay == "A":
        if playerPlay == "X":
            WinLossPts = 3
            SelectionPts = 1
        if playerPlay == "Y":
            WinLossPts = 6
            SelectionPts = 2
        if playerPlay == "Z":
            WinLossPts = 0
            SelectionPts = 3
    if oppositionPlay == "B":
        if playerPlay == "X":
            WinLossPts = 0
            SelectionPts = 1
        if playerPlay == "Y":
            WinLossPts = 3
            SelectionPts = 2
        if playerPlay == "Z":
            WinLossPts = 6
            SelectionPts = 3
    if oppositionPlay == "C":
        if playerPlay == "X":
            WinLossPts = 6
            SelectionPts = 1
        if playerPlay == "Y":
            WinLossPts = 0
            SelectionPts = 2
        if playerPlay == "Z":
            WinLossPts = 3
            SelectionPts = 3

    return WinLossPts + SelectionPts

def CalculateRoundScore2(oppositionPlay, desiredResult):
    if desiredResult == 'X': #Loss
        WinLossPts = 0
        if oppositionPlay == 'A': #Rock
            SelectionPts = 3
        if oppositionPlay == 'B': #Paper
            SelectionPts = 1
        if oppositionPlay == 'C': #Scissors
            SelectionPts = 2
    if desiredResult == 'Y': #Draw
        WinLossPts = 3
        if oppositionPlay == 'A': #Rock
            SelectionPts = 1
        if oppositionPlay == 'B': #Paper
            SelectionPts = 2
        if oppositionPlay == 'C': #Scissors
            SelectionPts = 3
    if desiredResult == 'Z': #Win
        WinLossPts = 6
        if oppositionPlay == 'A': #Rock
            SelectionPts = 2
        if oppositionPlay == 'B': #Paper
            SelectionPts = 3
        if oppositionPlay == 'C': #Scissors
            SelectionPts = 1

    return WinLossPts + SelectionPts

    

import os

here = os.path.dirname(os.path.abspath(__file__))

input = r"PuzzleInput.txt"

filename = os.path.join(here, input)

with open(filename) as fp:
    roundList = [p.strip() for p in fp.read().split('\n\n')]

roundScore1 = 0

for round in roundList:
    roundOverall = round.split('\n')
    for roundSplit in roundOverall:        
        oppositionPlay = roundSplit.split(' ')[0]
        playerPlay = roundSplit.split(' ')[1]

        roundScore1 += CalculateRoundScore1(oppositionPlay, playerPlay)

print(roundScore1)

# Part II
roundScore2 = 0

for round in roundList:
    roundOverall = round.split('\n')
    for roundSplit in roundOverall:
        oppositionPlay = roundSplit.split(' ')[0]
        desiredResult = roundSplit.split(' ')[1]

        roundScore2 += CalculateRoundScore2(oppositionPlay, desiredResult)

print(roundScore2)



