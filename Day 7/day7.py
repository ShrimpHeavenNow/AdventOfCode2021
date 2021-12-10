crabs = [int(x) for x in open('crabs.txt').read().strip().split(',')]


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


def PartTwoSmart(crabs):
    for x in crabs:
        x ^ 2 + x / 2  # Let's do some mean and median action tomorrow, wh?


PartOne(crabs)
# PartTwo(crabs)
