from copy import deepcopy
import math
import numpy as np
from utils import readFile, typeWrapper, Node, Dijkstra

data = readFile("input18.txt")
cubes = set()

for line in data:
    newLine = f"({line})"
    cubes.add(eval(newLine))

minX = min([cube[0] for cube in cubes]) - 1
maxX = max([cube[0] for cube in cubes]) + 1
xRange = (minX, maxX)
minY = min([cube[1] for cube in cubes]) - 1
maxY = max([cube[1] for cube in cubes]) + 1
yRange = (minY, maxY)
minZ = min([cube[2] for cube in cubes]) - 1
maxZ = max([cube[2] for cube in cubes]) + 1
zRange = (minZ, maxZ)
ranges = (xRange, yRange, zRange)

outside = set((1, 1, 1))
outsideList = [[1, 1, 1]]

sides = 0

while len(outsideList) != 0:
    cube = outsideList.pop(0)
    for side in range(len(cube)):
        dimRange = ranges[side]
        for change in [-1, 1]:
            cube[side] += change
            cubeTuple = tuple(cube)
            cube[side] -= change
            if cubeTuple[side] < dimRange[0] or cubeTuple[side] > dimRange[1]:
                continue
            elif cubeTuple in cubes:
                sides += 1
            elif cubeTuple in outside:
                continue
            else:
                outside.add(cubeTuple)
                outsideList.append(list(cubeTuple))
                


# sides = 6 * len(cubes)

# for cube in cubes:
#     cubeList = list(cube)
#     for side in range(len(cube)):
#         for change in [-1, 1]:
#             cubeList[side] += change
#             cubeTuple = tuple(cubeList) 
#             if cubeTuple in cubes:
#                 sides -= 1
#             cubeList[side] -= change


print(sides)