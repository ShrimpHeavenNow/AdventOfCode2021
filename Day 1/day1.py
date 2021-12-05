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


print(DayOne(sweeps))
