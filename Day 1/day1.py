with open('sonar.txt') as f:
    sweeps = [int(line.rstrip()) for line in f]


def DayOne(text):
    depth = 0
    depthChanges = -1  # To ignore the initial comparison.
    for x in text:
        if x > depth:
            depthChanges += 1
        depth = x
    return depthChanges

def PartTwo(text):
    x = 0
    y = 0
    firstSet = 0
    secondSet = 0
    sets = []
    depthChanges = 0
    for i in text:
        sets.append(text[x:x + 3])
        x += 1
    for i in range(len(sets)-1):
        for i in sets[y]:
            firstSet += i
        for i in sets[y+1]:
            secondSet += i
        if firstSet < secondSet:
            depthChanges += 1
        y += 1
        firstSet = 0
        secondSet = 0
    return depthChanges

print("Day One Part One answer:")
print(DayOne(sweeps))

print("Day One Part Two answer:")
print(PartTwo(sweeps))
