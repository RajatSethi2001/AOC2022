from copy import deepcopy
import math
import numpy as np
from utils import readFile, typeWrapper, Node

data = readFile("input.txt")

blocked = set()
maxDepth = 0
for line in data:
    points = line.split(" -> ")
    for pointIndex in range(len(points)-1):
        point1 = eval(f"[{points[pointIndex]}]")
        point2 = eval(f"[{points[pointIndex+1]}]")

        if point1[1] > maxDepth:
            maxDepth = point1[1]
        if point2[1] > maxDepth:
            maxDepth = point2[1]

        while point1 != point2:
            blocked.add(tuple(point1))
            if point1[0] != point2[0]:
                point1[0] += np.sign(point2[0] - point1[0])
            elif point1[1] != point2[1]:
                point1[1] += np.sign(point2[1] - point1[1])
        
        blocked.add(tuple(point2))

full = False
sands = 0
while not full:
    frozen = False
    sand = [500, 0]
    while not frozen:
        if sand[1] + 1 == maxDepth + 2:
            frozen = True
        elif (sand[0], sand[1] + 1) not in blocked:
            sand[1] += 1
        elif (sand[0] - 1, sand[1] + 1) not in blocked:
            sand[0] -= 1
            sand[1] += 1
        elif (sand[0] + 1, sand[1] + 1) not in blocked:
            sand[0] += 1
            sand[1] += 1
        else:
            frozen = True
    
    blocked.add(tuple(sand))
    sands += 1
    if (500, 0) in blocked:
        full = True      

print(sands) 
