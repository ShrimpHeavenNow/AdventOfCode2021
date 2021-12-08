with open('report.txt') as f:
    bits = [line.rstrip() for line in f]

fart = bits
butts = bits


def PartOne(text):
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


def Compare(thelist, compare):
    pos = 0
    remove = []
    while len(thelist) > 1:
        for x in remove:
            thelist.remove(x)
        remove = []
        for x in thelist:
            if x[pos] != compare[pos]:
                remove.append(x)
        pos += 1
    return thelist


def PartTwo(list):  # this can be wildly optimized.
    pos = 0

    while len(list) > 1:
        counts = 0
        remove = []
        compare = "0"
        for x in list:
            if x[pos] == "1":  # find the most popular bit in a position with a tie, decide on 1.
                counts += 1
        if counts > len(list) / 2 or counts == len(list) / 2:
            compare = "1"
        print("In Position " + str(pos) + " the more common bit is " + compare)
        print(len(list))
        for x in list:
            if x[pos] != compare:  # compare that bit to the list in that position
                remove.append(x)  # remove items that don't match
        for x in remove:
            list.remove(x)
        pos += 1  # Advance position

    print(list)


def PartTwo(list):  # this can be wildly optimized.
    pos = 0

    while len(list) > 1:
        counts = 0
        remove = []
        compare = "0"
        for x in list:
            if x[pos] == "1":  # find the most popular bit in a position with a tie, decide on 1.
                counts += 1
        if counts > len(list) / 2 or counts == len(list) / 2:
            compare = "1"
        # print("In Position "  + str(pos) + " the more common bit is " + compare)
        # print(len(list))
        for x in list:
            if x[pos] != compare:  # compare that bit to the list in that position
                remove.append(x)  # remove items that don't match
        for x in remove:
            list.remove(x)
        pos += 1  # Advance position

    return list[0]


def PartTwoTwo(list):  # There's gotta be a way to make this one function with PartTwo
    pos = 0

    while len(list) > 1:
        counts = 0
        remove = []
        compare = "0"
        for x in list:
            if x[pos] == "1":  # find the most popular bit in a position with a tie, decide on 1.
                counts += 1
        if counts > len(list) / 2 or counts == len(list) / 2:
            compare = "1"
        # print("In Position "  + str(pos) + " the more DICKS common bit is " + compare)
        # print(len(list))
        for x in list:
            if x[pos] == compare:  # compare that bit to the list in that position
                remove.append(x)  # remove items that don't match
        for x in remove:
            list.remove(x)
        pos += 1  # Advance position

    return list[0]


print("Power consumption: " + str(PartOne(bits)))

one = PartTwo(bits)

with open('report.txt') as f:  # There's probably some copy/ deepcopy fix for this..
    bits = [line.rstrip() for line in f]
two = PartTwoTwo(bits)

print(int(one, 2) * int(two, 2))
