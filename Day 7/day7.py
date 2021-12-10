import math

with open('crabs.txt') as f:
    crabs = [line.strip().split(',') for line in f]

crabs = crabs[0]  # See, I really need to learn how to parse more efficiently.
for i in range(0, len(crabs)):
    crabs[i] = int(crabs[i])


def PartOne(crabs):
    counts = {}
    for x in range(max(crabs)):
        count = 0
        for y in crabs:
            count += abs(x - y)
        counts[x] = count

    print(min(counts.values()))


def PartTwo(crabs):  # This is wildly inefficient, but hey: it works.
    counts = {}
    for x in range(max(crabs)):
        count = 0
        for y in crabs:
            for z in range(abs(x - y)):
                count += z + 1
        counts[x] = count

    print(min(counts.values()))


PartOne(crabs)
PartTwo(crabs)
