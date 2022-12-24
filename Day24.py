from copy import deepcopy
import math
import numpy as np
from utils import readFile, typeWrapper, Node, Dijkstra

import sys

data = readFile("input.txt")

minRow = 0
maxRow = len(data) - 1

minCol = 0
maxCol = len(data[0]) - 1

startPos = (0, 1)
endPos = (maxRow, maxCol - 1)

states = {}
blizzards = []
limit = 1000
sys.setrecursionlimit(limit + 10)

for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] in ['^', 'v', '>', '<']:
            blizzards.append([row, col, data[row][col]])

for minute in range(1, limit + 1):
    for blizzardIndex in range(len(blizzards)):
        blizzard = blizzards[blizzardIndex]
        if blizzard[2] == 'v':
            blizzard[0] += 1
        elif blizzard[2] == '^':
            blizzard[0] -= 1

        elif blizzard[2] == '<':
            blizzard[1] -= 1
        else:
            blizzard[1] += 1
        
        if blizzard[0] >= maxRow:
            blizzard[0] = minRow + 1
        elif blizzard[0] <= minRow:
            blizzard[0] = maxRow - 1

        if blizzard[1] >= maxCol:
            blizzard[1] = minCol + 1
        elif blizzard[1] <= minCol:
            blizzard[1] = maxCol - 1
    
    # stateCopy = deepcopy(blizzards)
    stateSet = set([(blizzard[0], blizzard[1]) for blizzard in blizzards])

    states[minute] = stateSet

def inBounds(pos):
    global minRow
    global maxRow
    global minCol
    global maxCol

    return (pos[0] > minRow and pos[0] < maxRow and pos[1] > minCol and pos[1] < maxCol) or pos == startPos or pos == endPos

winners = set()
contenders = set()
contenders.add((0, 1, 567))
minute = 0

while len(contenders) != 0:
    contenderList = list(contenders)
    sortedContenders = sorted(contenderList, key=lambda x:x[2])
    newWinner = sortedContenders[0]
    contenders.remove(newWinner)
    winners.add(newWinner)
    if (newWinner[0], newWinner[1]) == endPos:
        print(newWinner[2])
        exit()

    minute = newWinner[2]
    nextMinute = minute + 1 
    nextState = states[nextMinute]
    
    upPos = (newWinner[0] - 1, newWinner[1])
    if upPos not in nextState and inBounds(upPos):
        if (upPos[0], upPos[1], nextMinute) not in winners:
            contenders.add((upPos[0], upPos[1], nextMinute))
    
    downPos = (newWinner[0] + 1, newWinner[1])
    if downPos not in nextState and inBounds(downPos):
        if (downPos[0], downPos[1], nextMinute) not in winners:
            contenders.add((downPos[0], downPos[1], nextMinute))
    
    leftPos = (newWinner[0], newWinner[1] - 1)
    if leftPos not in nextState and inBounds(leftPos):
        if (leftPos[0], leftPos[1], nextMinute) not in winners:
            contenders.add((leftPos[0], leftPos[1], nextMinute))
    
    rightPos = (newWinner[0], newWinner[1] + 1)
    if rightPos not in nextState and inBounds(rightPos):
        if (rightPos[0], rightPos[1], nextMinute) not in winners:
            contenders.add((rightPos[0], rightPos[1], nextMinute))
    
    if (newWinner[0], newWinner[1]) not in nextState:
        if (newWinner[0], newWinner[1], nextMinute) not in winners:
            contenders.add((newWinner[0], newWinner[1], nextMinute))