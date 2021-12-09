with open('vents.txt') as f:
    vents = [line.strip() for line in f]
import numpy as np

lines = []


def Parse(line):
    # print(line)
    start, end = line.split(" -> ")
    x1, y1 = int(start.split(',')[0]), int(start.split(',')[1])
    x2, y2 = int(end.split(',')[0]), int(end.split(',')[1])
    # print(line)
    # print(x1)
    # print(y1)
    # print(x2)
    # print(y2)
    return x1, y1, x2, y2


def PartOne(lines):
    map = np.zeros(shape=(np.max(lines) + 1, np.max(lines) + 1))
    # print(map)
    for x in lines:
        if x[0] == x[2]:  # Mark horizontal line.
            print("Horizontal baby")  # +1 these coordinates in the array
            MarkArray(map, x, "horz")
        if x[1] == x[3]:  # Mark vertical line. This could probably combine with above.
            print("This bitch is vertical")  # +1 these coordinates in the array.
            MarkArray(map, x, "vert")
    overlaps = map[map > 1]
    print('The amount of overlaps is :' + str(len(overlaps)))


def MarkArray(array, line, dir):  # I have all the pieces but don't know how to put them together.
    if dir == "horz":
        steps = int(abs(line[2] - line[3]))
        print(line)
        print("steps")
        print(steps)
        for range
            print("a butt")
    if dir == "vert":
        steps = abs(line[0] - line[2])
        print(line)
        print("steps")
        print(steps)

print(vents)

for x in vents:
    lines.append(Parse(x))

PartOne(lines)
