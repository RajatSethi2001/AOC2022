from copy import deepcopy
import math
import numpy as np
from utils import readFile, typeWrapper, Node, Dijkstra

streams = list(readFile("input17.txt")[0])
for index in range(len(streams)):
    if streams[index] == "<":
        streams[index] = -1
    else:
        streams[index] = 1

rock1 = [[0, 0], [0, 1], [0, 2], [0, 3]]
rock2 = [[1, 0], [1, 1], [0, 1], [2, 1], [1, 2]]
rock3 = [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]
rock4 = [[0, 0], [1, 0], [2, 0], [3, 0]]
rock5 = [[0, 0], [1, 0], [0, 1], [1, 1]]
rocks = [rock1, rock2, rock3, rock4, rock5]

rockTower = set()
rockTemplate = {}

rockHeight = -1
streamIndex = 0

for index in range(10000):
    # print(index)
    currentRock = deepcopy(rocks[index % len(rocks)])
    for unit in currentRock:
        unit[1] += 2
        unit[0] += rockHeight + 4
    
    falling = True
    while falling:
        #MOVE LEFT/RIGHT
        stream = streams[streamIndex % len(streams)]
        streamIndex += 1

        failed = False
        for unit in currentRock:
            unit[1] += stream
            if unit[1] < 0 or unit[1] > 6 or tuple(unit) in rockTower:
                failed = True
        
        if failed:
            for unit in currentRock:
                unit[1] -= stream
        
        # MOVE DOWN
        failed = False
        for unit in currentRock:
            unit[0] -= 1
            if unit[0] < 0 or tuple(unit) in rockTower:
                failed = True
        
        if failed:
            falling = False
            for unit in currentRock:
                unit[0] += 1
                if unit[0] > rockHeight:
                    rockHeight = unit[0]
                rockTower.add(tuple(unit))
            rockTemplate[index] = currentRock

startRock = rockTemplate[9999]
trueRockDiff = 0
trueRowDiff = 0
for rockIndex in range(9989, -1, -5):
    testRock = rockTemplate[rockIndex]
    rowDiff = startRock[0][0] - testRock[0][0]
    fakeStart = deepcopy(startRock)
    for unit in fakeStart:
        unit[0] -= rowDiff
    
    if fakeStart == testRock:
        rockDiff = 9999 - rockIndex
        for compareIndex in range(rockDiff):
            ogRock = rockTemplate[9999 - rockDiff]
            copyRock = rockTemplate[rockIndex - rockDiff]
            if ogRock[0][1] != copyRock[0][1] or ogRock[0][0] - rowDiff != copyRock[0][0]:
                break
        else:
            trueRockDiff = rockDiff
            trueRowDiff = rowDiff
            break

rocksLeft = 10 ** 12 - 10000
rockCopyHeight = (rocksLeft // trueRockDiff) * trueRowDiff
rocksExtra = rocksLeft % trueRockDiff

for index in range(rocksExtra):
    # print(index)
    currentRock = deepcopy(rocks[index % len(rocks)])
    for unit in currentRock:
        unit[1] += 2
        unit[0] += rockHeight + 4
    
    falling = True
    while falling:
        #MOVE LEFT/RIGHT
        stream = streams[streamIndex % len(streams)]
        streamIndex += 1

        failed = False
        for unit in currentRock:
            unit[1] += stream
            if unit[1] < 0 or unit[1] > 6 or tuple(unit) in rockTower:
                failed = True
        
        if failed:
            for unit in currentRock:
                unit[1] -= stream
        
        # MOVE DOWN
        failed = False
        for unit in currentRock:
            unit[0] -= 1
            if unit[0] < 0 or tuple(unit) in rockTower:
                failed = True
        
        if failed:
            falling = False
            for unit in currentRock:
                unit[0] += 1
                if unit[0] > rockHeight:
                    rockHeight = unit[0]
                rockTower.add(tuple(unit))
            rockTemplate[index] = currentRock

print(rockHeight + rockCopyHeight + 1)

