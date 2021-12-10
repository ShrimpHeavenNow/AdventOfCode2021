crabs = [int(x) for x in open('crabs.txt').read().strip().split(',')]


def PartOne(crabs):
    counts = {}
    for x in range(min(crabs), max(crabs)):
        count = 0
        for y in crabs:
            count += abs(x - y)
        counts[x] = count

    print(min(counts.values()))


def PartTwo(crabs):  # This is wildly inefficient, but hey: it works.
    counts = {}
    for x in range(min(crabs), max(crabs)):
        count = 0
        for y in crabs:
            for z in range(abs(x - y)):
                count += z + 1
        counts[x] = count

    print(min(counts.values()))


def Fuel(z):
    z = z * (z + 1) // 2
    return z


def PartTwoSmart(crabs):
    costs = []
    for x in crabs:
        cost = 0
        for y in crabs:
            cost += Fuel(abs(x - y))
        costs.append(cost)
    print(min(costs))


PartOne(crabs)
# PartTwo(crabs)
PartTwoSmart(crabs)
