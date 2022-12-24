from utils import readFile, typeWrapper

data = readFile("input.txt")

line = data[0]

window = list(line[0:14])
for char in range(len(line[14::])):
    window.pop(0)
    window.append(line[char + 14])

    if len(set(window)) == 14:
        print(char + 15)
        break