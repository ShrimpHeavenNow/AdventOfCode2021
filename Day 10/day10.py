with open('syntax.txt') as f:
    lines = [line.strip() for line in f]


def PartOne(lines):
    opens = ('(', '[', '<', '{')
    closes = (')', ']', '>', '}')
    corruptions = []
    for x in lines:
        inside = []
        for y in x:
            if y in opens:
                inside.append(y)
            if y in closes:
                if opens.index(inside[-1:][0]) != closes.index(y):
                    corruptions.append(y)
                    print(x,"is corrupted")
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
toremove = []
for x in lines:  # Remove Corrupted.
    inside = []
    for y in x:
        if y in opens:
            inside.append(y)
        if y in closes:
            if opens.index(inside[-1:][0]) != closes.index(y):
                toremove.append(x)
                print(x,"is corrupted")
                break
            else:
                inside.pop()

for x in toremove:  # There's a better way of doing this I'm sure.
    lines.remove(x)

pointValues = {"(": 1, "[": 2, "{": 3, "<": 4}
scores = []
for x in lines:  # A smart person could do this in one iteration, I bet. Anyway, here's scoring.
    score = 0
    inside = []
    for y in x:
        if y in opens:
            inside.append(y)
        else:
            inside.pop()
    inside.reverse()
    for y in inside:
        score = (score * 5)
        score += pointValues[y]
    scores.append(score)

scores.sort()
mid = len(scores)//2
print(scores)
print(scores[mid])
