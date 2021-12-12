with open('syntax.txt') as f:
    lines = [line.strip() for line in f]


def PartOne(lines):
    opens = ('(', '[', '<', '{')
    closes = (')', ']', '>', '}')
    inside = []
    corruptions = []
    for x in lines:
        inside = []
        for y in x:
            if y in opens:
                inside.append(y)
            if y in closes:
                if opens.index(inside[-1:][0]) != closes.index(y):
                    corruptions.append(y)
                    break
                else:
                    inside.pop()

    print(corruptions)
    pointValues = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    for x in corruptions:
        score += pointValues[x]
    print(score)


PartOne(lines)

opens = ('(', '[', '<', '{')
closes = (')', ']', '>', '}')
inside = []
corruptions = []
print(len(lines))
for x in lines:
    inside = []
    for y in x:
        if y in opens:
            inside.append(y)
        if y in closes:
            if opens.index(inside[-1:][0]) != closes.index(y):
                corruptions.append(y)
                lines.remove(x)
                break
            else:
                inside.pop()


pointValues = {")": 1, "]": 2, "}": 3, ">": 4}
score = 0
for x in corruptions:
    score += pointValues[x]
print(score)
