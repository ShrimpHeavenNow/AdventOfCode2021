heightmap = {}

with open("floor.txt") as file:
    for x, line in enumerate(file):
        for y, c in enumerate(line.strip()):
            heightmap[(x, y)] = int(c)

maximum = (x, y)


def GetAdjacents(coords, maximums):
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


lows = []

for this_loc in heightmap:
    is_local_minimum = True
    for adj in GetAdjacents(this_loc, maximum):
        if heightmap[this_loc] >= heightmap[adj]:
            # If we find a lower adjacent coord, this isn't a local
            # minimum and we can stop checking.
            is_local_minimum = False
            break
    if is_local_minimum:
        lows.append(this_loc)

risk = 0

for x in lows:
    risk += 1 + heightmap[x]
print(risk)

visited = []


def Basins(coords, maximums, visited, heightmap):
    adjacents = GetAdjacents(coords, maximums)
    size = 1
    for chud in adjacents:
        if chud not in visited:
            visited.append(chud)
            if heightmap[chud] != 9:
                size += Basins(chud, maximums, visited, heightmap)
    return size


basinSizes = []

for x in lows:
    visited.append(x)
    basinSizes.append(Basins(x, maximum, visited, heightmap))
basinSizes.sort(reverse=True)

print(basinSizes[0] * basinSizes[1] * basinSizes[2])

"""
Most of this code was copied from  hugseverycat. I had made a part one that worked fine, but I got so lost in the
weeds for part 2. I knew I needed to do a recursive thing. My problem was I was worrying about keeping the values
instead of just the coords. I also was trying to iterate over the hole map instead of just the lowpoints. Biggest
problem was not also having a seperate function for finding adjacents. I learned a lot from this bad boy.

"""