from utils import readFile, typeWrapper

data = readFile("input.txt")

subAss = 0
for ass in data:
    splitAss = ass.split(",")
    splitAss1 = splitAss[0].split("-")
    splitAss2 = splitAss[1].split("-")
    min1 = int(splitAss1[0])
    max1 = int(splitAss1[1])
    min2 = int(splitAss2[0])
    max2 = int(splitAss2[1])

    range1 = set(range(min1, max1+1))
    range2 = set(range(min2, max2+1))

    if len(range1.intersection(range2)) > 0:
        subAss += 1

print(subAss)
