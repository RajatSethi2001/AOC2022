from utils import readFile, typeWrapper, Node

data = readFile("input.txt")
for line in range(len(data)):
    data[line] = list(data[line])
    for value in range(len(data[line])):
        data[line][value] = int(data[line][value])

visible = 0
best_score = 0
for row in range(len(data)):
    for col in range(len(data[row])):
        score = 1
        tree = data[row][col]

        dist = 0
        for new_row in range(row-1, -1, -1):
            dist += 1
            if data[new_row][col] >= tree:
                break
        if dist == 0:
            dist = 1
        score *= dist

        dist = 0
        for new_row in range(row+1, len(data)):
            dist += 1
            if data[new_row][col] >= tree:
                break
        if dist == 0:
            dist = 1
        score *= dist

        dist = 0
        for new_col in range(col-1, -1, -1):
            dist += 1
            if data[row][new_col] >= tree:
                break
        if dist == 0:
            dist = 1
        score *= dist

        dist = 0
        for new_col in range(col+1, len(data[row])):
            dist += 1
            if data[row][new_col] >= tree:
                break
        if dist == 0:
            dist = 1
        score *= dist

        if score > best_score:
            best_score = score

print(best_score)