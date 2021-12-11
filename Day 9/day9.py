with open('floortest.txt') as f:
    floor = [line.strip() for line in f]


def split(word):  # This is both stupid and neat.
    y = [int(char) for char in word]
    y.insert(0, 9)
    y.append(9)
    return y


floor2 = []
for x in floor:  # If I weren't an idiot, I could do this in one line.
    x = split(x)
    floor2.append((x))
floor2.insert(0, [9 for x in range(0, len(floor2[0]) + 2)])
floor2.append(floor2[0])


def PartOne(floor):
    ypos = 1
    lowpoints = []
    for x in floor[1:-1]:
        xpos = 0
        for y in x:
            if y != 9:
                if y < floor[ypos][xpos - 1] and y < floor[ypos][xpos + 1] and y < floor[ypos + 1][xpos] and y < \
                        floor[ypos - 1][xpos]:
                    lowpoints.append(y + 1)
            xpos += 1
        ypos += 1
    print(sum(lowpoints))  # Having a list and summing was better for debugging. Why am I justifying myself?


def FindNines(floor, xpos, ypos, areacoords):
    xmax = len(floor[0])
    ymax = len(floor)
    print(ypos)
    print(xpos)
    print(floor[ypos][xpos])
    print(areacoords)
    if floor[ypos - 1][xpos - 1] != 9:  # Find way to not go beyond 0 or max
        if (ypos - 1, xpos - 1) not in areacoords.keys():
            areacoords[(ypos - 1, xpos - 1)] = False
    if floor[ypos + 1][xpos - 1] != 9:
        if (ypos + 1, xpos - 1) not in areacoords.keys():
            areacoords[(ypos - 1, xpos - 1)] = False
    if floor[ypos - 1][xpos + 1] != 9:
        if (ypos - 1, xpos + 1) not in areacoords.keys():
            areacoords[(ypos - 1, xpos + 1)] = False
    if floor[ypos + 1][xpos + 1] != 9:
        if (ypos + 1, xpos + 1) not in areacoords.keys():
            areacoords[(ypos + 1, xpos + 1)] = False
    areacoords[(ypos, xpos)] = True
    for x in areacoords:  # do FindNines to all the falses.
        if floor[x[0]][x[1]] == 9:
            print("WHAT THE HELL")
        elif areacoords[x] == False:
            FindNines(floor, x[0], x[1], areacoords)

    return areacoords

        # make a dict of coords with value of checked or not. add unchecked adjacent non-9s to dict. check all non checked.
        # Once fully checked, return the full list


def PartTwo(floor):

    ypos = 1
    areasizes = []
    for z in floor[1:-1]:
        areacoords = {}
        xpos = 1
        for d in z:
            areacoords[(ypos, xpos)] = False
            areacoords = FindNines(floor, xpos, ypos, areacoords)
            xpos += 1
            areasizes.append(len(areacoords))
            for i in areacoords.keys():
                y = i[0]
                x = i[1]
                floor[y][x] = 9  # This is either smart or really dumb.
        ypos += 1
    print(sum(areasizes))


    """
    So we need to find an area surrounded by nines.
    find the amount of numbers in that area
    add that to a list to later multiply.

    TO find an area surrounded by nines, we iterate through a list and see if it has a 9 next to it then see if its
    adjacents also have 9s.

    recursion?
    """


PartOne(floor2)
PartTwo(floor2)
