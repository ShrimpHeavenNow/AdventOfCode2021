with open('submoves.txt') as f:
    moves = [line.rstrip() for line in f]

def PartOne(moves):
    x = 0
    y = 0
    for i in moves:
        if i[0] == "f":
            x += int(i[-1])
        if i[0] == "u":
            y -= int(i[-1])
        if i[0] == "d":
            y += int(i[-1])
        location = x * y
    return location

def PartTwo(moves):
    x = 0
    y = 0
    aim = 0
    for i in moves:
        if i[0] == "f":
            x += int(i[-1])
            y += int(i[-1]) * aim
        if i[0] == "u":
            aim -= int(i[-1])
        if i[0] == "d":
            aim += int(i[-1])
        location = x * y
    return location

print("Part One Answer:")
print(PartOne(moves))
print("Part Two Answer:")
print(PartTwo(moves))