with open('report.txt') as f:
    bits = [line.rstrip() for line in f]


def PartOne(text):  # There's a way to do this without the dict. There's also a way to auto generate this dict.
    counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
    gamma = ""
    epsil = ""
    for x in text:
        for y in range(len(x)):
            if x[y] == "1":
                counts[y] += 1
    for x in counts.values():
        if x > len(text) / 2:
            gamma += "1"
            epsil += "0"
        else:
            gamma += "0"
            epsil += "1"
    return int(gamma, 2) * int(epsil, 2)


def PartTwo(Oxygen):  # this can be wildly optimized.
    pos = 0
    while len(Oxygen) > 1:
        counts = 0
        remove = []
        compare = "0"  # There's a smart way to not need this, I'm sure of it.
        for x in Oxygen:
            if x[pos] == "1":  # find the most popular bit in a position with a tie, decide on 1.
                counts += 1
        if counts > len(Oxygen) / 2 or counts == len(Oxygen) / 2:
            compare = "1"
        for x in Oxygen:
            if x[pos] != compare:  # compare that bit to the list in that position
                remove.append(x)  # remove items that don't match
        for x in remove:
            Oxygen.remove(x)
        pos += 1  # Advance position

    return Oxygen[0]


def PartTwoTwo(carbon):  # There's gotta be a way to make this one function with PartTwo
    pos = 0

    while len(carbon) > 1:
        counts = 0
        remove = []
        compare = "0"
        for x in carbon:
            if x[pos] == "1":
                counts += 1
        if counts > len(carbon) / 2 or counts == len(carbon) / 2:
            compare = "1"
        for x in carbon:
            if x[pos] == compare:  # This is the only change from PartTwo (Can operators be arguments?)
                remove.append(x)
        for x in remove:
            carbon.remove(x)
        pos += 1

    return carbon[0]


print("Power consumption: " + str(PartOne(bits)))

one = PartTwo(bits)

with open('report.txt') as f:  # There's probably some copy/ deepcopy fix for this.
    bits = [line.rstrip() for line in f]

two = PartTwoTwo(bits)

print("Life Support Rating: " + str(int(one, 2) * int(two, 2)))
