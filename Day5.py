from utils import readFile, typeWrapper
import numpy as np

data = readFile("input.txt")

rows = []
columns = []
line = "temp"

index = 0
while line != "":
    line = data[index]
    # line = line.replace("] [", "]|[")
    line = line.replace("    ", " [X]")
    row = line.split(" ")
    rows.append(row)
    index += 1

del rows[len(rows) - 1]
del rows[len(rows) - 1]

columns = np.array(rows).T.tolist()

for column in range(len(columns)):
    columns[column] = [col for col in columns[column] if col != '[X]']

while index < len(data):
    instr = data[index].split(" ")
    amt = int(instr[1])
    old = int(instr[3]) - 1
    new = int(instr[5]) - 1

    loc = 0
    for _ in range(amt):
        columns[new].insert(loc, columns[old].pop(0))
        loc += 1
    
    index += 1

for col in columns:
    print(col[0])
    
