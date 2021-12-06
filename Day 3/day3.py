with open('report.txt') as f:
    bits = [line.rstrip() for line in f]

counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}

def PartOne(text):
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


print("Power consumption: " + str(PartOne(bits)))
