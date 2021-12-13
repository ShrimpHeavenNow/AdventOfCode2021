# This seems a lot like day 9. find adjacents and recurse.
# perform the steps after nothing is left in the "adjacents" pool
import self as self




class octopus:  # Might not be needed...
    def __init__(self, energy, coords):
        self.energy = energy
        self.coords = coords

    def Flash(self, maximums, dumbos, flashes, visited):  # Checks if the dumbo should flash. engergizes adjacents.

        if self.energy == 10:  # Checks if flashes
            adjacents = GetAdjacents(self.coords, maximums) # Gets adjacent octopuses coordinates
            flashes += 1  # Adds to the flash total
            for chud in adjacents:
                if chud not in visited:  # If the neighbor hasn't received the flash yet
                    visited.append(chud)  # Add to visited list
                    for x in dumbos:
                        if x.coords == chud:  # Matches octopus to coordinate (sloppy, I know)
                            if x.energy < 10:  # If it's not 10, adds one
                                x.energy += 1
                            if x.energy == 10:  # Flashes if it's 10. Should this be elif?
                                x.Flash(maximums, dumbos, flashes, visited)
        return flashes



def GetAdjacents(coords, maximums):
    xcoords, ycoords = coords
    xmax, ymax = maximums
    adjacent = []
    if xcoords < xmax:  # Check if this coord is the right edge
        adjacent.append((xcoords + 1, ycoords))
        if ycoords < ymax:
            adjacent.append((xcoords + 1, ycoords + 1))
        if ycoords > 0:  # Check if it's the top
            adjacent.append((xcoords + 1, ycoords - 1))
    if xcoords > 0:  # Check if it's the left edge
        adjacent.append((xcoords - 1, ycoords))
        if ycoords < ymax:
            adjacent.append((xcoords - 1, ycoords + 1))
        if ycoords > 0:  # Check if it's the top
            adjacent.append((xcoords - 1, ycoords - 1))
    if ycoords < ymax:  # Check if it's the bottom
        adjacent.append((xcoords, ycoords + 1))
    if ycoords > 0:  # Check if it's the top
        adjacent.append((xcoords, ycoords - 1))

    return adjacent

def PartOne():
    octopi = []
    with open("octopitest.txt") as file:
        for x, line in enumerate(file):  # Is this better than an array?
            for y, c in enumerate(line.strip()):
                octopi.append(octopus(int(c), (x, y)))
    maximum = (x, y)
    flashes = 0
    totalFlashes = 0

    for z in range(100):
        print("step", z)
        visited = []
        for x in octopi:
            x.energy += 1
        for x in octopi:
            flashes = 0
            visited.append(x.coords)
            flashes = x.Flash(maximum, octopi, flashes, visited)
            totalFlashes += flashes
        for x in octopi:
            if x.energy == 10:
                x.energy = 0
        totalFlashes += flashes
        print("total", totalFlashes)

# PartOne()

with open('octopitest.txt') as f:
    octopi = [line.strip() for line in f]
octopi2 = []

for x in octopi:  # If I weren't an idiot, I could do this in one line.
    octopi3 = []
    for y in x:
        octopi3.append(int(y))
    octopi2.append(octopi3)
maximums = [len(octopi2[0]), len(octopi2)]

for x in octopi2:
    for y in x:
        adjacent = GetAdjacents([octopi2.index((x)),x.index(y)], maximums)





