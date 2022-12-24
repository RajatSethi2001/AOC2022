from copy import deepcopy
import math
import numpy as np
from utils import readFile, typeWrapper, Node, Dijkstra

data = readFile("input21.txt")

monkeys = {}
for line in data:
    monkey = line.split(": ")
    if monkey[0] == "root":
        equation = monkey[1].split(" ")
        equation[1] = "="
        monkey[1] = " ".join(equation)
    try:
        monkey[1] = int(monkey[1])
    except:
        pass
    monkeys[monkey[0]] = monkey[1]

def monkeyYell(monkey):
    if isinstance(monkeys[monkey], int):
        return monkeys[monkey]
    else:
        operations = monkeys[monkey].split(" ")
        op1 = monkeyYell(operations[0])
        op2 = monkeyYell(operations[2])
        operand = operations[1]
        equation = f"op1 {operand} op2"
        return eval(equation)

# print(monkeyYell("root"))

def monkeyValue(getMonkey):
    for depMonkey in monkeys:
        if not isinstance(monkeys[depMonkey], int) and getMonkey in monkeys[depMonkey]:
            operations = monkeys[depMonkey].split(" ")
            op1 = operations[0]
            op2 = operations[2]
            operand = operations[1]

            if depMonkey == "root":
                if op1 == getMonkey:
                    return monkeyYell(op2)
                else:
                    return monkeyYell(op1)
            
            elif op1 == getMonkey:
                trueOp1 = monkeyValue(depMonkey)
                trueOp2 = monkeyYell(op2)
                if operand == "+":
                    return eval(f"trueOp1 - trueOp2")
                elif operand == "-":
                    return eval(f"trueOp1 + trueOp2")
                elif operand == "*":
                    return eval(f"trueOp1 / trueOp2")
                elif operand == "/":
                    return eval(f"trueOp1 * trueOp2")
                else:
                    print("uh oh")
                    exit()
            else:
                trueOp1 = monkeyValue(depMonkey)
                trueOp2 = monkeyYell(op1)
                if operand == "+":
                    return eval(f"trueOp1 - trueOp2")
                elif operand == "-":
                    return eval(f"trueOp2 - trueOp1")
                elif operand == "*":
                    return eval(f"trueOp1 / trueOp2")
                elif operand == "/":
                    return eval(f"trueOp2 / trueOp1")
                else:
                    print("uh oh 2")
                    exit()

print(monkeyValue("humn"))