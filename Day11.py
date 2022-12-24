from utils import readFile, typeWrapper, Node
import math

with open("input.txt", "r") as f:
    data = f.read()

data = data.split("\n\n")

class Monkey:
    def __init__(self):
        self.items = []
        self.operation = None
        self.test = None
        self.throwTrue = None
        self.throwFalse = None
        self.inspects = 0

monkeys = []
for monkey in data:
    monkeyData = monkey.split("\n")
    for index in range(len(monkeyData)):
        monkeyData[index] = monkeyData[index].lstrip().rstrip()
    
    newMonkey = Monkey()
    newMonkey.items = [int(item) for item in monkeyData[1].split(": ")[1].split(", ")]
    newMonkey.operation = " ".join(monkeyData[2].split(": ")[1].split(" ")[2::])
    newMonkey.test = int(monkeyData[3].split(" ")[-1])
    newMonkey.throwTrue = int(monkeyData[4].split(" ")[-1])
    newMonkey.throwFalse = int(monkeyData[5].split(" ")[-1])
    monkeys.append(newMonkey)

testList = [monkey.test for monkey in monkeys]
monkeyProd = 1
for test in testList:
    monkeyProd *= test

for _ in range(10000):
    for monkey in monkeys:
        while len(monkey.items) != 0:
            monkey.inspects += 1
            old = monkey.items.pop(0)
            new = round(eval(monkey.operation))
            if new % monkey.test == 0:
                newMonkey = monkeys[monkey.throwTrue]
            else:
                newMonkey = monkeys[monkey.throwFalse]
            
            new = new % newMonkey.test

            newMonkey.items.append(new)

sortMonkey = sorted(monkeys, key=lambda x: x.inspects, reverse=True)
total = sortMonkey[0].inspects * sortMonkey[1].inspects

print(total)