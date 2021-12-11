with open('floor.txt') as f:
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


def PartTwo(floor):
    """
    So we need to find an area surrounded by nines.
    find the amount of numbers in that area
    add that to a list to later multiply.

    TO find an area surrounded by nines, we iterate through a list and see if it has a 9 next to it.
    """


PartOne(floor2)
PartTwo(floor2)
