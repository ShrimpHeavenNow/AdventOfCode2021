with open('signals.txt') as f:
    signals = [line.strip().split(' ') for line in f]


def MeetsCOnditions(x):
    if len(x) == 3 or len(x) == 4 or len(x) == 2 or len(x) == 7:
        return True


def PartOne(signals):  # 1 = 2, 7 = 3, 4 = 4 8 = 7
    count = 0
    for x in signals:
        for y in x[-4:]:
            if MeetsCOnditions(y):
                count += 1
    print(count)


def PartTwoCorrect(signals):
    segments = []
    for x in signals:
        fives = []
        sixes = []
        display = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
        for z in x[:10]:
            if len(z) == 2:
                display[1] = set(z)
            if len(z) == 4:
                display[4] = set(z)
            if len(z) == 3:
                display[7] = set(z)
            if len(z) == 7:
                display[8] = set(z)
            if len(z) == 5:
                fives.append(z)
            if len(z) == 6:
                sixes.append(z)
        for y in fives:
            if display[7].issubset(y):
                display[3] = set(y)
            elif len(set(y).intersection(display[4])) == 3:
                display[5] = set(y)
            else:
                display[2] = set(y)
        for y in sixes:
            if display[4].issubset(y):
                display[9] = set(y)
            elif display[7].issubset(y):
                display[0] = set(y)
            else:
                display[6] = set(y)
        segment = ''

        for y in x[-4:]:
            y = set(y)
            for i, key in enumerate(display.values()):
                if y == key:
                    segment += str(i)
        segments.append(int(segment))
    print(sum(segments))


PartOne(signals)
PartTwoCorrect(signals)
