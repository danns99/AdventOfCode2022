# Part I
def CalculatePriority(character):
    if character == 'a':
        Priority = 1
    if character == 'b':
        Priority = 2
    if character == 'c':
        Priority = 3
    if character == 'd':
        Priority = 4
    if character == 'e':
        Priority = 5
    if character == 'f':
        Priority = 6
    if character == 'g':
        Priority = 7
    if character == 'h':
        Priority = 8
    if character == 'i':
        Priority = 9
    if character == 'j':
        Priority = 10
    if character == 'k':
        Priority = 11
    if character == 'l':
        Priority = 12
    if character == 'm':
        Priority = 13
    if character == 'n':
        Priority = 14
    if character == 'o':
        Priority = 15
    if character == 'p':
        Priority = 16
    if character == 'q':
        Priority = 17
    if character == 'r':
        Priority = 18
    if character == 's':
        Priority = 19
    if character == 't':
        Priority = 20
    if character == 'u':
        Priority = 21
    if character == 'v':
        Priority = 22
    if character == 'w':
        Priority = 23
    if character == 'x':
        Priority = 24
    if character == 'y':
        Priority = 25
    if character == 'z':
        Priority = 26
    if character == 'A':
        Priority = 27
    if character == 'B':
        Priority = 28
    if character == 'C':
        Priority = 29
    if character == 'D':
        Priority = 30
    if character == 'E':
        Priority = 31
    if character == 'F':
        Priority = 32
    if character == 'G':
        Priority = 33
    if character == 'H':
        Priority = 34
    if character == 'I':
        Priority = 35
    if character == 'J':
        Priority = 36
    if character == 'K':
        Priority = 37
    if character == 'L':
        Priority = 38
    if character == 'M':
        Priority = 39
    if character == 'N':
        Priority = 40
    if character == 'O':
        Priority = 41
    if character == 'P':
        Priority = 42
    if character == 'Q':
        Priority = 43
    if character == 'R':
        Priority = 44
    if character == 'S':
        Priority = 45
    if character == 'T':
        Priority = 46
    if character == 'U':
        Priority = 47
    if character == 'V':
        Priority = 48
    if character == 'W':
        Priority = 49
    if character == 'X':
        Priority = 50
    if character == 'Y':
        Priority = 51
    if character == 'Z':
        Priority = 52

    return Priority

import os

here = os.path.dirname(os.path.abspath(__file__))

input = r"PuzzleInput.txt"

filename = os.path.join(here, input)

with open(filename) as fp:
    rucksackList = [p.strip() for p in fp.read().split('\n')]

sumDuplicateCharacterPriority = 0

for rucksack in rucksackList:
    rucksack1 = rucksack[0:len(rucksack)//2]
    rucksack2 = rucksack[len(rucksack)//2:]

    duplicateCharacter = ''

    for character in rucksack1:
        if character in rucksack2:
            duplicateCharacter = character

    duplicateCharacterPriority = CalculatePriority(duplicateCharacter)

    sumDuplicateCharacterPriority += duplicateCharacterPriority

print(sumDuplicateCharacterPriority)

# Part II
sumDuplicateCharacterPriority = 0

for i in range(0,len(rucksackList),3):
    elf1 = rucksackList[i]
    elf2 = rucksackList[i+1]
    elf3 = rucksackList[i+2]

    duplicateCharacter = ''

    for character in elf1:
        if character in elf2:
            if character in elf3:
                duplicateCharacter = character

    duplicateCharacterPriority = CalculatePriority(duplicateCharacter)

    sumDuplicateCharacterPriority += duplicateCharacterPriority

print(sumDuplicateCharacterPriority)