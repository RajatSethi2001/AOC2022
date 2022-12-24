from copy import deepcopy
import math
import numpy as np
from utils import readFile, typeWrapper, Node, Dijkstra

data = readFile("input22.txt")

maxLen = 0
ins = data.pop()
data.pop()

ins = ins.replace("R", " R ").replace("L", " L ").split(" ")

for line in data:
    if len(line) > maxLen:
        maxLen = len(line)

bounds = {}
for line in range(len(data)):
    bounds[line] = [0, 0]
    if len(data[line]) < maxLen:
        bounds[line][1] = len(data[line])
        difference = maxLen - len(data[line])
        data[line] = data[line] + "T" * difference
    else:
        bounds[line][1] = maxLen
    
    for col in range(maxLen):
        if data[line][col] == " ":
            fakeData = list(data[line])
            fakeData[col] = "T"
            data[line] = "".join(fakeData)
            bounds[line][0] += 1
    bounds[line][0] -= 1

rowBounds = {}
for col in range(len(data[0])):
    rowBounds[col] = [0, len(data) - 1]
    for row in range(len(data)):
        if data[row][col] == "T":
            rowBounds[col][0] += 1
        else:
            rowBounds[col][0] -= 1
            break
    
    for row in range(len(data) - 1, -1, -1):
        if data[row][col] == "T":
            rowBounds[col][1] -= 1
        else:
            rowBounds[col][1] += 1
            break

faces = {}
faces[1] = [[0, 49], [100, 149]]
faces[2] = [[0, 49], [50, 99]]
faces[3] = [[50, 99],[50, 99]]
faces[4] = [[100, 149], [50, 99]]
faces[5] = [[100, 149], [0, 49]]
faces[6] = [[150, 199], [0, 49]]

def getFace(pos):
    global faces
    for face in faces:
        if pos[0] >= faces[face][0][0] and pos[0] <= faces[face][0][1] and pos[1] >= faces[face][1][0] and pos[1] <= faces[face][1][1]:
            return face 

# writeFile = open("fakeInput.txt", "w")
# for line in data:
#     writeFile.write(line + "\n")

# print(rowBounds)

pos = [0, bounds[0][0]+1]
dir = 0
for i in ins:
    if i == "R":
        dir = (dir + 1) % 4
    elif i == "L":
        dir = (dir - 1) % 4
    else:
        i = int(i)
        # RIGHT
        for _ in range(i):
            if dir == 0:
                og = deepcopy(pos)
                pos[1] += 1
                line = pos[0]
                if pos[1] >= bounds[line][1]:
                    face = getFace(og)
                    relRow = pos[0] - faces[face][0][0]
                    print("Right " + str(relRow))
                    if face == 1:
                        #Face 4 - CHECK
                        dir = 2
                        pos[0] = 149 - relRow
                        pos[1] = 99
                    elif face == 3:
                        #Face 1 - CHECK
                        dir = 3 
                        pos[0] = 49
                        pos[1] = 100 + relRow
                    elif face == 4:
                        #Face 1 - 
                        dir = 2
                        pos[0] = 49 - relRow
                        pos[1] = 149
                    elif face == 6:
                        #Face 4
                        dir = 3
                        pos[0] = 149
                        pos[1] = 50 + relRow

                if data[pos[0]][pos[1]] == "#":
                    pos = og
                    dir = 0
                    break

            elif dir == 1:
                # DOWN
                og = deepcopy(pos)
                pos[0] += 1
                col = pos[1]
                if pos[0] >= rowBounds[col][1]:
                    face = getFace(og)
                    relCol = pos[1] - faces[face][1][0]
                    print("Down " + str(relCol))
                    if face == 1:
                        #Face 3
                        dir = 2
                        pos[0] = 50 + relCol
                        pos[1] = 99
                    elif face == 4:
                        #Face 6
                        dir = 2
                        pos[0] = 150 + relCol
                        pos[1] = 49
                    elif face == 6:
                        #Face 1
                        pos[0] = 0
                        pos[1] = 100 + relCol
                
                if data[pos[0]][pos[1]] == "#":
                    pos = og
                    dir = 1
                    break

            elif dir == 2:
                # LEFT
                og = deepcopy(pos)
                pos[1] -= 1
                line = pos[0]
                if pos[1] <= bounds[line][0]:
                    face = getFace(og)
                    relRow = pos[0] - faces[face][0][0]
                    print("Left " + str(relRow))
                    if face == 2:
                        #Face 5
                        dir = 0
                        pos[0] = 149 - relRow
                        pos[1] = 0
                    elif face == 3:
                        #Face 5
                        dir = 1
                        pos[0] = 100
                        pos[1] = relRow
                    elif face == 5:
                        #Face 2
                        dir = 0
                        pos[0] = 49 - relRow
                        pos[1] = 50
                    elif face == 6:
                        #Face 2
                        dir = 1
                        pos[0] = 0
                        pos[1] = 50 + relRow

                if data[pos[0]][pos[1]] == "#":
                    pos = og
                    dir = 2
                    break
            else:
            # UP
                og = deepcopy(pos)
                pos[0] -= 1
                col = pos[1]
                if pos[0] <= rowBounds[col][0]:
                    face = getFace(og)
                    relCol = pos[1] - faces[face][1][0]
                    print("Up " + str(relCol))
                    if face == 1:
                        #Face 6
                        pos[0] = 199
                        pos[1] = relCol
                    elif face == 2:
                        #Face 6
                        dir = 0
                        pos[0] = 150 + relCol
                        pos[1] = 0
                    elif face == 5:
                        #Face 3
                        dir = 0
                        pos[0] = 50 + relCol
                        pos[1] = 50
                
                if data[pos[0]][pos[1]] == "#":
                    pos = og
                    dir = 3
                    break

print((pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + dir)