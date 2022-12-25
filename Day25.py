from copy import deepcopy
import math
import numpy as np
from utils import readFile, typeWrapper, Node, Dijkstra

data = readFile("input.txt")

def SNAFUtoDec(snafu):
    base = 1
    dec = 0
    for digitIndex in range(len(snafu) - 1, -1, -1):
        digit = snafu[digitIndex]
        digitDec = None
        if digit == "=":
            digitDec = -2
        elif digit == "-":
            digitDec = -1
        else:
            digitDec = eval(digit)
        
        dec += base * digitDec
        base *= 5
    return dec

def DectoSNAFU(dec):
    exp = 0
    digitNext = {"2": "1", "1": "0", "0": "-", "-": "=", "=": None}
    digitPrev = {"=": "-", "-": "0", "0": "1", "1": "2", "2": None}
    while dec > 5 ** exp:
        exp += 1
    
    digits = ["2" for _ in range(exp + 1)]
    SNAFUstr = "".join(digits)
    SNAFU = SNAFUtoDec(SNAFUstr)
    digitIndex = 0
    while SNAFU != dec:
        if SNAFU > dec:
            nextDigit = digitNext[digits[digitIndex]]
            if nextDigit is None:
                digitIndex += 1
            else:
                digits[digitIndex] = nextDigit
        
        elif SNAFU < dec:
            prevDigit = digitPrev[digits[digitIndex]]
            digits[digitIndex] = prevDigit
            digitIndex += 1
        
        SNAFUstr = "".join(digits)
        SNAFU = SNAFUtoDec(SNAFUstr)
    
    return SNAFUstr

totalSum = 0
for snafu in data:
    totalSum += SNAFUtoDec(snafu)

print(totalSum)
print(DectoSNAFU(totalSum))
