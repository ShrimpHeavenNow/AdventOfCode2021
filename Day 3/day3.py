with open('report.txt') as f:
    bits = [line.rstrip() for line in f]


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


def PartTwoWRONG(text):  # There's a way to just use the part one function.
    thelist = text
    counts = 0
    gamma = ""
    epsil = ""
    oxy = text
    carbon = text
    remove = []
    pos = 0
    while len(thelist) >1:

        for x in thelist:
            if x[pos] == "1":
                counts += 1
        if counts > len(thelist) /2:
            for x in thelist:
                if x[pos] == "0":
                    remove.append(x)  # Why can't I wrap my mind around this?
    pos +=1


    print(gamma)  # Use this for finding O2
    print(epsil)  # Use this for CO2

    print("Final oxy is: " + str(Compare(oxy, gamma)))
    print("Final carbon is: " + str(Compare(carbon, epsil)))
    return int(oxy[0], 2) * int(carbon[0], 2)


print("Power consumption: " + str(PartOne(bits)))
print("Life Support Rating: " + str(PartTwo(bits)))
