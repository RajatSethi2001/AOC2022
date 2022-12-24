from copy import deepcopy
import math
import numpy as np
from utils import readFile, typeWrapper, Node, Dijkstra

data = readFile("input23.txt")
elves = set()

for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] == "#":
            elves.add((row, col))

def checkLocs(newLocs):
    global elves
    for newLoc in newLocs:
        if newLoc in elves:
            return False
    
    return True

order = ["north", "south", "west", "east"]
round = 1
while True:
    movements = {}
    for elf in elves:
        row = elf[0]
        col = elf[1]

        north = checkLocs([(row - 1, col), (row - 1, col - 1), (row - 1, col + 1)])
        east = checkLocs([(row, col + 1), (row + 1, col + 1), (row - 1, col + 1)])
        south = checkLocs([(row + 1, col), (row + 1, col - 1), (row + 1, col + 1)])
        west = checkLocs([(row, col - 1), (row + 1, col - 1), (row - 1, col - 1)])

        if north and east and south and west:
            continue
        
        newLoc = None
        direction = None
        for checkDir in order:
            if eval(checkDir):
                direction = checkDir
                break
        else:
            continue
        
        if direction == "north":
            newLoc = (row - 1, col)
        elif direction == "south":
            newLoc = (row + 1, col)
        elif direction == "west":
            newLoc = (row, col - 1)
        elif direction == "east":
            newLoc = (row, col + 1)

        if newLoc in movements:
            movements[newLoc].append((row, col))
        else:
            movements[newLoc] = [(row, col)]
    
    firstDir = order.pop(0)
    order.append(firstDir)
    move = False
    for newLoc in movements:
        if len(movements[newLoc]) == 1:
            elves.remove(movements[newLoc][0])
            elves.add(newLoc)
            move = True
    
    if not move:
        print(round)
        exit()
    else:
        round += 1

minRow = 100000
maxRow = 0

minCol = 100000
maxCol = 0

for elf in elves:
    row = elf[0]
    col = elf[1]

    if row < minRow:
        minRow = row
    
    if row > maxRow:
        maxRow = row
    
    if col < minCol:
        minCol = col
    
    if col > maxCol:
        maxCol = col
    
height = (maxRow - minRow + 1)
width = (maxCol - minCol + 1)

print(elves)

rectArea = height * width
emptySquares = rectArea - len(elves)
print(emptySquares)
    
