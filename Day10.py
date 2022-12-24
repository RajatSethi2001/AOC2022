from utils import readFile, typeWrapper, Node

data = readFile("input.txt")

x = 1
cycleNum = 1
insIndex = 0
in_progress = False
sig = []
to_do = []

lit = []
row = []
while insIndex < len(data):
    if not in_progress:
        ins = data[insIndex].split(" ")
        if ins[0] == "addx":
            to_do = [int(ins[1]), 2]
            in_progress = True
        insIndex += 1
        
    cycleLoc = cycleNum % 40 - 1
    if cycleLoc == 0 and cycleNum != 1:
        lit.append(row)
        row = []
    
    if cycleLoc in [x-1, x, x+1]:
        row.append("#")
    else:
        row.append(".")

    if (cycleNum - 20) % 40 == 0:
        sig.append(cycleNum * x)
    cycleNum += 1

    if in_progress:
        to_do[1] -= 1
        if to_do[1] == 0:
            in_progress = False
            x += to_do[0]
            to_do = []

lit.append(row)
for row in lit:
    for char in row:
        print(char + " ",end="")
    print()