from utils import readFile, typeWrapper

data = readFile("input.txt")

sum = 0
for sack in range(0, len(data), 3):
    part1 = set(data[sack])
    part2 = set(data[sack+1])
    part3 = set(data[sack+2])
    common = (part1.intersection(part2).intersection(part3).pop()).swapcase()
    if common.isupper():
        sum += ord(common) - 64
    else:
        sum += ord(common) - 70

print(sum)
