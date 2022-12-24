from copy import deepcopy
import math
import numpy as np
from utils import readFile, typeWrapper, Node, Dijkstra

data = readFile("input.txt")

blueprints = []
for line in data:
    blueprintData = line.split(" ")
    blueprint = {}
    blueprint["ore"] = int(blueprintData[6])
    blueprint["clay"] = int(blueprintData[12])
    blueprint["obs"] = (int(blueprintData[18]), int(blueprintData[21]))
    blueprint["geode"] = (int(blueprintData[27]), int(blueprintData[30]))
    blueprints.append(blueprint)

bestGeodes = 0
minuteMax = 26
checkpoints = {}

maxOre = None
maxClay = None
maxObs = None
def runPrint(blueprint, ore, clay, obs, geode, minutes):
    global bestGeodes
    global minuteMax
    global checkpoints

    global maxOre
    global maxClay
    global maxObs

    newMinutes = minutes + 1

    oreBuildable = ore[1] >= blueprint["ore"] and ore[0] < maxOre
    clayBuildable = ore[1] >= blueprint["clay"] and clay[0] < maxClay
    obsBuildable = ore[1] >= blueprint["obs"][0] and clay[1] >= blueprint["obs"][1] and obs[0] < maxObs
    geodeBuildable = ore[1] >= blueprint["geode"][0] and obs[1] >= blueprint["geode"][1]

    #Bot + Current Materials
    newOre = ore[1] + ore[0]
    newClay = clay[1] + clay[0]
    newObs = obs[1] + obs[0]
    newGeode = geode[1] + geode[0]

    if newMinutes >= minuteMax:
        if newGeode > bestGeodes:
            bestGeodes = newGeode
        return

    remainder = minuteMax - newMinutes
    maxPossible = newGeode + (remainder * geode[1]) + (remainder * (remainder + 1)) / 2
    # for newMin in range(1, remainder+1):
    #     maxPossible += geode[1] + newMin
    
    if maxPossible <= bestGeodes:
        return
    
    # for minute in range(1, newMinutes + 1):
    #     if ore[0] <= checkpoints[minute][0] and \
    #         clay[0] <= checkpoints[minute][1] and \
    #         obs[0] <= checkpoints[minute][2] and \
    #         geode[0] <= checkpoints[minute][3] and \
    #         newOre <= checkpoints[minute][4] and \
    #         newClay <= checkpoints[minute][5] and \
    #         newObs <= checkpoints[minute][6] and \
    #         newGeode <= checkpoints[minute][7]:
    #         return
    
    # if ore[0] >= checkpoints[newMinutes][0] and \
    #     clay[0] >= checkpoints[newMinutes][1] and \
    #     obs[0] >= checkpoints[newMinutes][2] and \
    #     geode[0] >= checkpoints[newMinutes][3] and \
    #     newOre >= checkpoints[newMinutes][4] and \
    #     newClay >= checkpoints[newMinutes][5] and \
    #     newObs >= checkpoints[newMinutes][6] and \
    #     newGeode >= checkpoints[newMinutes][7]:
    #     checkpoints[newMinutes] = (ore[0], clay[0], obs[0], geode[0], newOre, newClay, newObs, newGeode)

    runPrint(blueprint, (ore[0], newOre), (clay[0], newClay), (obs[0], newObs), (geode[0], newGeode), newMinutes)

    if oreBuildable:
        runPrint(blueprint, (ore[0] + 1, newOre - blueprint["ore"]), (clay[0], newClay), (obs[0], newObs), (geode[0], newGeode), newMinutes)

    if clayBuildable:
        runPrint(blueprint, (ore[0], newOre - blueprint["clay"]), (clay[0] + 1, newClay), (obs[0], newObs), (geode[0], newGeode), newMinutes)

    if obsBuildable:
        runPrint(blueprint, (ore[0], newOre - blueprint["obs"][0]), (clay[0], newClay - blueprint["obs"][1]), (obs[0] + 1, newObs), (geode[0], newGeode), newMinutes)

    if geodeBuildable:
        runPrint(blueprint, (ore[0], newOre - blueprint["geode"][0]), (clay[0], newClay), (obs[0], newObs - blueprint["geode"][1]), (geode[0] + 1, newGeode), newMinutes)

geodeProduct = 1
qualitySum = 0
for index in range(len(blueprints)):
    print(index + 1)
    blueprint = blueprints[index]
    maxOre = max(blueprint["ore"], blueprint["clay"], blueprint["obs"][0], blueprint["geode"][0])
    maxClay = blueprint["obs"][1]
    maxObs = blueprint["geode"][1]

    bestGeodes = 0
    runPrint(blueprint, (1, 0), (0, 0), (0, 0), (0, 0), 0)
    print(bestGeodes)
    geodeProduct *= bestGeodes
    qualitySum += (index + 1) * bestGeodes

print(geodeProduct)
print(qualitySum)