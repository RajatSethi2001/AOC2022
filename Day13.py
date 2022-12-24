import copy
import math
import numpy as np
from utils import readFile, typeWrapper, Node

data = readFile("input.txt")
packets = [[[2]], [[6]]]
pairs = []
for line in range(0, len(data), 3):
    data[line] = eval(data[line])
    data[line+1] = eval(data[line+1])
    packets.append(data[line])
    packets.append(data[line+1])
    pair = [data[line], data[line+1]]
    pairs.append(pair)

def compareLists(list1, list2):
    for index in range(min(len(list1), len(list2))):
        if isinstance(list1[index], int) and isinstance(list2[index], int):
            if list1[index] > list2[index]:
                return False
            elif list1[index] < list2[index]:
                return True
            
        elif isinstance(list1[index], list) and isinstance(list2[index], list):
            rightOrder = compareLists(list1[index], list2[index])
            if rightOrder is not None:
                return rightOrder
        
        elif isinstance(list1[index], int) and isinstance(list2[index], list):
            newList = [list1[index]]
            rightOrder = compareLists(newList, list2[index])
            if rightOrder is not None:
                return rightOrder
        
        else:
            newList = [list2[index]]
            rightOrder = compareLists(list1[index], newList)
            if rightOrder is not None:
                return rightOrder
        
    if len(list1) > len(list2):
        return False
    elif len(list1) < len(list2):
        return True
    
    return None

# pairIndices = 0
# for pair in range(len(pairs)):
#     list1 = pairs[pair][0]
#     list2 = pairs[pair][1]
    

#     rightOrder = False
#     rightOrder = compareLists(list1, list2)
#     if rightOrder is True:
#         pairIndices += pair + 1

# print(pairIndices)

for packet1 in range(len(packets)):
    for packet2 in range(packet1 + 1, len(packets)):
        list1 = copy.deepcopy(packets[packet1])
        list2 = copy.deepcopy(packets[packet2])

        rightOrder = compareLists(list1, list2)

        if rightOrder is False:
            packets[packet1] = list2
            packets[packet2] = list1

div1 = packets.index([[2]]) + 1
div2 = packets.index([[6]]) + 1

print(div1 * div2)