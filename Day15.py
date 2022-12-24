from copy import deepcopy
import math
import numpy as np
from utils import readFile, typeWrapper, Node

data = readFile("input.txt")

sensors = {}
no_beacons = set()

def manhat(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

sensorRange = {}

limit = 4000000
# limit = 20
trueInterval = set(range(0, limit+1))
for line in data:
    splitLine = line.split(" ")
    senseX = int(splitLine[2][2:len(splitLine[2]) - 1])
    senseY = int(splitLine[3][2:len(splitLine[3]) - 1])
    beacX = int(splitLine[8][2:len(splitLine[8]) - 1])
    beacY = int(splitLine[9][2:len(splitLine[9])])
    
    sensors[(senseX, senseY)] = (beacX, beacY)

    dist = manhat((senseX, senseY), (beacX, beacY))

    # row = 2000000
    # if (senseY <= row and senseY + dist >= row) or (senseY >= row and senseY - dist <= row):
    #     remainder = abs(dist - abs(senseY-row))
    #     for col in range(-remainder, remainder+1):
            
    #         newX = senseX + col
    #         # newY = senseY + row
    #         no_beacons.add((newX, row))
    
    # if ((beacX, beacY) in no_beacons):
    #     no_beacons.remove((beacX, beacY))

    print(line)
    for row in range(max(0, senseY-dist), min(limit+1, senseY+dist+1)):
        remainder = abs(dist - abs(senseY-row))
        colRange =  [max(0, senseX-remainder), min(limit, senseX + remainder)]

        if row in sensorRange:
            sensorRange[row].append(colRange)
        else:
            sensorRange[row] = [colRange]
    



for row in sensorRange:
    print(row)
    sortRange = sorted(sensorRange[row], key=lambda x: x[0])
    rangeStart = sortRange[0][0]
    rangeEnd = sortRange[0][1]

    for interval in sortRange[1::]:
        if interval[0] <= rangeEnd+1:
            if interval[1] >= rangeEnd:
                rangeEnd = interval[1]
        else:
            print((interval[0] - 1) * 4000000 + row)
            exit()
    
    # for colRange in sensorRange[row]:
    #     interval = interval.union(set(range(colRange[0], colRange[1])))
    # interval = sensorRange[row]
    # if len(interval) != limit + 1:
    #     print(trueInterval.difference(interval), row)
    #     exit()
