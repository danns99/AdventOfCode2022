import os

here = os.path.dirname(os.path.abspath(__file__))

input = r"PuzzleInput.txt"

filename = os.path.join(here, input)

with open(filename, 'r') as f:
    messageString = f.readlines()
    messageString = [entry for entry in messageString]

    messageCharacters = list(messageString[0])

#Part I

for messageIndex in range(3,len(messageCharacters),1):
    bufferString = [messageCharacters[messageIndex-3], messageCharacters[messageIndex-2], messageCharacters[messageIndex-1], messageCharacters[messageIndex]]

    if bufferString.count(bufferString[0]) == 1 | bufferString.count(bufferString[1]) == 1 | bufferString.count(bufferString[2]) == 1 | bufferString.count(bufferString[3]) == 1:
        break

print(str(messageIndex+1) + ' characters need to be processed before the first start-of-packet marker is detected')

#Part II

for messageIndex in range(13,len(messageCharacters),1):
    bufferString = [messageCharacters[messageIndex-13], messageCharacters[messageIndex-12], messageCharacters[messageIndex-11], messageCharacters[messageIndex-10],
                    messageCharacters[messageIndex-9], messageCharacters[messageIndex-8], messageCharacters[messageIndex-7], messageCharacters[messageIndex-6],
                    messageCharacters[messageIndex-5], messageCharacters[messageIndex-4], messageCharacters[messageIndex-3], messageCharacters[messageIndex-2],
                    messageCharacters[messageIndex-1], messageCharacters[messageIndex]]

    print(bufferString)

    if bufferString.count(bufferString[0]) == 1 | bufferString.count(bufferString[1]) == 1 | bufferString.count(bufferString[2]) == 1 | bufferString.count(bufferString[3]) == 1  | bufferString.count(bufferString[4]) == 1 | bufferString.count(bufferString[5]) == 1 | bufferString.count(bufferString[6]) == 1 | bufferString.count(bufferString[7]) == 1  | bufferString.count(bufferString[8]) == 1 | bufferString.count(bufferString[9]) == 1 | bufferString.count(bufferString[10]) == 1 | bufferString.count(bufferString[11]) == 1  | bufferString.count(bufferString[12]) == 1 | bufferString.count(bufferString[13]) == 1:
        break

print(str(messageIndex+1) + ' characters need to be processed before the first start-of-packet marker is detected')