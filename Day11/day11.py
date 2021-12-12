# This seems a lot like day 9. find adjacents and recurse.
# perform the steps after nothing is left in the "adjacents" pool
octopi = {}
with open("octopitest.txt") as file:
    for x, line in enumerate(file):  # Is this better than an array?
        for y, c in enumerate(line.strip()):
            octopi[(x, y)] = int(c)
print(octopi)
maximum = (x, y)


def GetAdjacents(coords, maximums):  # TODO: Add diagonals
    xcoords, ycoords = coords
    xmax, ymax = maximums
    adjacent = []
    if xcoords < xmax:  # Check if this coord is the right edge
        adjacent.append((xcoords + 1, ycoords))
    if xcoords > 0:  # Check if it's the left edge
        adjacent.append((xcoords - 1, ycoords))
    if ycoords < ymax:  # Check if it's the bottom
        adjacent.append((xcoords, ycoords + 1))
    if ycoords > 0:  # Check if it's the top
        adjacent.append((xcoords, ycoords - 1))
    return adjacent
