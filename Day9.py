from utils import readFile, typeWrapper, Node
import copy

data = readFile("input.txt")

pos = [[0, 0] for _ in range(10)]
tailLoc = set()
for line in data:
    command = line.split(" ")
    dir = command[0]
    dist = int(command[1])

    for move in range(dist):
        if dir == "R":
            pos[0][0] += 1
        elif dir == "U":
            pos[0][1] += 1
        elif dir == "L":
            pos[0][0] -= 1
        else:
            pos[0][1] -= 1
        
        for tail in range(1, len(pos)):
            delta_x = pos[tail-1][0] - pos[tail][0]
            delta_y = pos[tail-1][1] - pos[tail][1]
            if abs(delta_x) <= 1 and abs(delta_y) <= 1:
                continue
            
            pos[tail][0] += delta_x // max(abs(delta_x), 1)
            pos[tail][1] += delta_y // max(abs(delta_y), 1)
        
        tailLoc.add(tuple(pos[9]))

print(len(tailLoc)) 