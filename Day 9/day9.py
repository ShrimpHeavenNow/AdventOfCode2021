with open('floortest.txt') as f:
    floor = [line.strip()for line in f]
print(floor)

def split(word):
    return [int(char) for char in word]

floor2 =[]
for x in floor:    # If I weren't an idiot, I could do this in one line.
    x = split(x)
    floor2.append((x))

print(floor2[1][3])