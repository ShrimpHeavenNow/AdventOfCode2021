with open('vents.txt') as f:
    vents = [line.strip() for line in f]
import numpy as np
from skimage.draw import line  # Thank god I found this.

lines = []  # I don't see other people doing this which makes me think it's wrong.


def Parse(line):
    start, end = line.split(" -> ")
    x1, y1 = int(start.split(',')[0]), int(start.split(',')[1])
    x2, y2 = int(end.split(',')[0]), int(end.split(',')[1])
    return x1, y1, x2, y2


def PartOne(lines):  # Who needs a part 2 anyway?
    map1 = np.zeros(shape=(np.max(lines) + 1, np.max(lines) + 1))  # This used to be its own function
    map2 = np.zeros(shape=(np.max(lines) + 1, np.max(lines) + 1))  # Oh, how much I've grown, what a fool I was.
    for x in lines:
        x1, y1, x2, y2 = x
        rr, cc = line(x1, y1, x2, y2)  # Originally I was painstakingly iterating through coordinates.
        if x1 == x2 or y1 == y2:
            map1[rr, cc] += 1
        map2[rr, cc] += 1
    overlaps1 = map1[map1 > 1]
    overlaps2 = map2[map2 > 1]
    print("Part one overlaps: " + str(len(overlaps1)))
    print("Part two overlaps: " + str(len(overlaps2)))


for x in vents:
    lines.append(Parse(x))

PartOne(lines)
