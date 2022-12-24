from utils import readFile, typeWrapper

data = readFile("input.txt")
print(data)
sums = []
elf = 0
for item in data:
    if item is '':
        sums.append(elf)
        elf = 0
    else:
        elf += int(item)

sums = sorted(sums)
sums.reverse()

print(sum(sums[0:3]))