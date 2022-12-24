from copy import deepcopy
import math
import numpy as np
from utils import readFile, typeWrapper, Node, Dijkstra

data = readFile("input20.txt")
data = typeWrapper(data, int)

dataNums = [[data[index] * 811589153, index] for index in range(len(data))]
total = len(data)
for _ in range(10):
    for index in range(len(dataNums)):
        currentIndex = dataNums[index][1]
        x = dataNums[index][0]
        trueChange = x % (total - 1)
        bonus = 0
        if (currentIndex + trueChange) >= total:
            bonus = 1
        elif (currentIndex + trueChange) < 0:
            bonus = -1
        newIndex = (currentIndex + trueChange + bonus) % total

        dataNums[index][1] = newIndex
        for otherIndex in set(range(len(dataNums))).difference(set([index])):
            if dataNums[otherIndex][1] > currentIndex:
                dataNums[otherIndex][1] -= 1
        
        for otherIndex in set(range(len(dataNums))).difference(set([index])):
            if dataNums[otherIndex][1] >= newIndex:
                dataNums[otherIndex][1] += 1

newData = sorted(dataNums, key=lambda x: x[1])
zeroIndex = None
for value in newData:
    if value[0] == 0:
        zeroIndex = value[1]
        break

num1 = newData[(zeroIndex + 1000) % total][0]
num2 = newData[(zeroIndex + 2000) % total][0]
num3 = newData[(zeroIndex + 3000) % total][0]
print(num1, num2, num3, sum([num1, num2, num3]))