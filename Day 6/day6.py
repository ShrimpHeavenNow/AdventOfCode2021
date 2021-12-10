with open('fish.txt') as f:
    fish = [line.strip().split(',') for line in f]  # HOW DO I ELEGANTLY MAKE THESE INTS!? GOD DAMN.


def Parse(list):  # This is so god-damn unnecessary.
    betterList = []
    for x in list:
        for y in x:
            betterList.append(int(y))
    return betterList


class lanterns:  # I could have created the columns here instead of doing it with every win check.
    def __init__(self, spawnTimer, isNew):
        self.spawnTimer = spawnTimer
        self.isNew = isNew

    def Spawn(self, spawnList):
        if self.spawnTimer == -1:
            spawnList.append(lanterns(9, True))
            self.spawnTimer = 6
            self.isNew = False
        return spawnList


def PartTwo(fishies, days):
    fish = [fishies.count(i) for i in range(9)]
    for i in range(days):
        num = fish.pop(0)
        fish[6] += num
        fish.append(num)
        assert len(fish) == 9
    print(sum(fish))


def PartOne(spawns, days):
    lanternFish = []
    for x in spawns:
        lanternFish.append(lanterns(x, False))
    timers = []
    for x in lanternFish:
        timers.append(x.spawnTimer)
    for x in range(days):
        timers = []
        for y in lanternFish:
            y.spawnTimer -= 1
            y.Spawn(lanternFish)
            timers.append(y.spawnTimer)

    print(len(lanternFish))


fish = Parse(fish)

PartOne(fish, 80)  # Fun fact, not scalable.

PartTwo(fish, 256)
