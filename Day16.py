from copy import deepcopy
import math
import numpy as np
from utils import readFile, typeWrapper, Node, Dijkstra


#SOLUTION SO I DON'T FORGET IT
#Find shortest path between every (non-zero) node + start-node and every other (non-zero) node
#Actions become either turn on valve or go to another non-zero node
#Remove actions if you've already turned on the valve or already visted that node

data = readFile("input.txt")

valves = {}
validValves = set()
validFlows = {}

for line in data:
    splitLine = line.replace(",", "").split(" ")
    valve = splitLine[1]
    flow = int(splitLine[4][5:len(splitLine[4])-1])
    leads = set(splitLine[9::])
    
    valveNode = Node()
    valveNode.id = valve
    valveNode.data["flow"] = flow
    if flow != 0:
        validValves.add(valve)
    valveNode.data["neighbors"] = leads 
    valves[valve] = valveNode

maxFlow = 0
for valve in valves:
    valveNode = valves[valve]
    maxFlow += valveNode.data["flow"]
    for neighbor in valveNode.data["neighbors"]:
        valveNode.children.append([valves[neighbor], 1])

shortestPath = {}
for valve in valves:
    winners = Dijkstra(valves[valve])
    shortestPath[valve] = winners

bestOutput = 0
minuteMax = 27
bestVisits = {}
def valveOpen(humanValve, humanDist, humanDest, elephantValve, elephantDist, elephantDest, minutes, pressureRate, pressureTotal, visited):
    global bestOutput
    global minuteMax
    global maxFlow

    newMinutes = minutes + 1
    newTotal = pressureTotal + pressureRate

    # Reach the 30-minute mark
    if newMinutes >= minuteMax:
        if newTotal > bestOutput:
            bestOutput = newTotal
            print(bestOutput)
        return

    remainder = minuteMax - newMinutes + 1
    maxIncrease = maxFlow * remainder
    if newTotal + maxIncrease < bestOutput:
        return
    
    if humanDist - 1 > remainder and elephantDist - 1 > remainder:
        if newTotal + (pressureRate * remainder) < bestOutput:
            return
    
    if humanDist != 0 and elephantDist != 0:
        newHumanDist = humanDist - 1
        newElephantDist = elephantDist - 1
        
        valveOpen(humanValve, newHumanDist, humanDest, elephantValve, newElephantDist, elephantDest, newMinutes, pressureRate, newTotal, visited)
    
    elif humanDist == 0 and elephantDist != 0:
        newElephantDist = elephantDist - 1
        
        newValve = humanDest
        humanNode = valves[newValve]
        humanFlow = humanNode.data["flow"]
        newRate = pressureRate + humanFlow
        
        newLocations = validValves.difference(visited)
        
        if len(newLocations) == 0:
            valveOpen(newValve, 1000, None, elephantValve, newElephantDist, elephantDest, newMinutes, newRate, newTotal, visited)
        else:
            for location in newLocations:
                newHumanDist = shortestPath[newValve][location][1]
                newVisited = deepcopy(visited)
                newVisited.add(location)
                valveOpen(newValve, newHumanDist, location, elephantValve, newElephantDist, elephantDest, newMinutes, newRate, newTotal, newVisited)

    elif humanDist != 0 and elephantDist == 0:
        newHumanDist = humanDist - 1

        newValve = elephantDest

        elephantNode = valves[newValve]
        elephantFlow = elephantNode.data["flow"]
        newRate = pressureRate + elephantFlow
        
        newLocations = validValves.difference(visited)

        if len(newLocations) == 0:
            valveOpen(humanValve, newHumanDist, humanDest, newValve, 1000, None, newMinutes, newRate, newTotal, visited)
        else:
            for location in newLocations:
                newElephantDist = shortestPath[newValve][location][1]
                newVisited = deepcopy(visited)
                newVisited.add(location)
                valveOpen(humanValve, newHumanDist, humanDest, newValve, newElephantDist, location, newMinutes, newRate, newTotal, newVisited)

    else:  
        newHumanValve = humanDest
        newElephantValve = elephantDest

        humanNode = valves[newHumanValve]
        humanFlow = humanNode.data["flow"]

        elephantNode = valves[newElephantValve]
        elephantFlow = elephantNode.data["flow"]

        newRate = pressureRate + humanFlow + elephantFlow

        frozenVisited = frozenset(visited)
        frozenKey = (frozenVisited, newHumanValve, newElephantValve)
        if frozenKey not in bestVisits:
            bestVisits[frozenKey] = (newMinutes, newTotal)
        else:
            bestMinutes = bestVisits[frozenKey][0]
            bestTotal = bestVisits[frozenKey][1]
            if newMinutes > bestMinutes and newTotal < bestTotal:
                return
            elif newMinutes < bestMinutes and newTotal > bestTotal:
                bestVisits[frozenKey] = (newMinutes, newTotal)

        newLocations = validValves.difference(visited)
        if len(newLocations) == 0:
            valveOpen(newHumanValve, 1000, None, newElephantValve, 1000, None, newMinutes, newRate, newTotal, visited)
        elif len(newLocations) == 1:
            finalLocation = list(newLocations)[0]
            newVisited = deepcopy(visited)
            newVisited.add(finalLocation)

            newHumanDist = shortestPath[newHumanValve][finalLocation][1]
            newElephantDist = shortestPath[newElephantValve][finalLocation][1]
            valveOpen(newHumanValve, newHumanDist, finalLocation, newElephantValve, 1000, None, newMinutes, newRate, newTotal, newVisited)
            valveOpen(newHumanValve, 1000, None, newElephantValve, newElephantDist, finalLocation, newMinutes, newRate, newTotal, newVisited)
        else:
            for humanLocation in newLocations:
                for elephantLocation in newLocations.difference(set([humanLocation])):
                    newVisited = deepcopy(visited)
                    newVisited.add(humanLocation)
                    newVisited.add(elephantLocation)

                    newHumanDist = shortestPath[newHumanValve][humanLocation][1]
                    newElephantDist = shortestPath[newElephantValve][elephantLocation][1]
                    valveOpen(newHumanValve, newHumanDist, humanLocation, newElephantValve, newElephantDist, elephantLocation, newMinutes, newRate, newTotal, newVisited)
    
    if len(visited) == len(validValves):
        remainder = minuteMax - newMinutes
        finalTotal = newTotal + (pressureRate * remainder)
        if finalTotal > bestOutput:
            bestOutput = finalTotal
            print(bestOutput)
            return
    

valveOpen("AA", 0, "AA", "AA", 0, "AA", 0, 0, 0, set())
print(bestOutput)