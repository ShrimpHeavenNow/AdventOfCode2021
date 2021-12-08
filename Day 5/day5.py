with open('vents.txt') as f:
    vents = tuple(line.rstrip().split(" -> ") for line in f]
