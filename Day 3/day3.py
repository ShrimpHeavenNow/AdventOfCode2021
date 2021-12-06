with open('report.txt') as f:
    bits = [line.rstrip() for line in f]
print(len(bits))


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


def PartTwo(text):
    counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
    gamma = ""
    epsil = ""
    oxy = []
    carbon = []
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
    print(gamma)  # Use this for finding O2
    print(epsil)  # Use this for CO2

    for x in text:
         if x[0] == gamma[0]:
             oxy.append(x)  # Make list of popular numbers
         else:
             carbon.append(x)  # Make list of unpopular numbers
    print(len(oxy))
    print(len(carbon))
    pos = 1
    while len(oxy) > 1: # There's definitely a way to get both from one while...
        for x in oxy:
            print(x)
            if x[pos] != gamma[pos]:
                oxy.remove(x)
    print(len(oxy))
    pos += 1
    print("Final oxy is: " + str(oxy))
    while len(carbon) > 1:
        for x in carbon:
            if x[pos] != epsil[pos]:
                carbon.remove(x)
                print(x)
                print("NOPE!")
    print("Final carbon is: " + str(carbon))

print("Power consumption: " + str(PartOne(bits)))

PartTwo(bits)