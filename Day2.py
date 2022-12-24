from utils import readFile, typeWrapper

data = readFile("input.txt")

score = 0
for match in data:
    round = match.split(' ')
    opp = round[0]
    you = round[1]

    if opp == 'A':
        if you == 'X':
            score += 0 + 3
        elif you == 'Y':
            score += 3 + 1
        else:
            score += 6 + 2
    elif opp == 'B':
        if you == 'X':
            score += 0 + 1
        elif you == 'Y':
            score += 3 + 2
        else:
            score += 6 + 3
    else:
        if you == 'X':
            score += 0 + 2
        elif you == 'Y':
            score += 3 + 3 
        else:
            score += 6 + 1
print(score)