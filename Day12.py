import math
import numpy as np
from utils import readFile, typeWrapper, Node

data = readFile("input.txt")
grid = []
for line in data:
    grid.append(list(line))
grid = np.array(grid)

gridDir = []
for row in range(len(grid)):
    gridDir.append([])
    for col in range(len(grid[row])):
        gridDir[row].append('.')
gridDir = np.array(gridDir)

aLoc = np.where(np.logical_or(grid == 'a', grid == 'S'))
steps = []
for start in range(len(aLoc[0])):
    current = (aLoc[0][start], aLoc[1][start])
    winners = {current: 0}
    neighbors = {}
    while grid[current] != 'E':
        up = (current[0] - 1, current[1])
        down = (current[0] + 1, current[1])
        left = (current[0], current[1] - 1)
        right = (current[0], current[1] + 1)
        curNeigh = [up, down, left, right]
        for index in range(len(curNeigh)):
            n = curNeigh[index]
            if (np.array(n) < grid.shape).all() and (np.array(n) >= 0).all():
                if ((ord(grid[n]) - ord(grid[current])) <= 1 and grid[n] != 'E') or grid[current] in 'Sz':
                    if (n not in neighbors or winners[current] + 1 <= neighbors[n][0]) and n not in winners:
                        dir = '.'
                        if index == 0:
                            dir = '^'
                        elif index == 1:
                            dir = 'v'
                        elif index == 2:
                            dir = '<'
                        else:
                            dir = '>'
                        neighbors[n] = (winners[current] + 1, dir)
        
        neighborList = list(neighbors.items())
        if len(neighborList) == 0:
            break
        neighborList = sorted(neighborList, key=lambda x: x[1][0])
        
        current = neighborList[0][0]
        winners[current] = neighborList[0][1][0]
        dir = neighborList[0][1][1]
        if dir == '^':
            oldCur = (current[0] + 1, current[1])
        elif dir == 'v':
            oldCur = (current[0] - 1, current[1])
        elif dir == '<':
            oldCur = (current[0], current[1] + 1)
        else:
            oldCur = (current[0], current[1] - 1)
        gridDir[oldCur] = dir
        neighbors.pop(current)
        if grid[current] == 'E':
            steps.append(winners[current])
            break
        
print(min(steps))

