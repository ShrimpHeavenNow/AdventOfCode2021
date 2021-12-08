with open('bingo.txt') as f:
    bingo = [line.rstrip() for line in f]

for x in bingo:
    if x == "":
        bingo.remove(x)


class board:  # I could have created the columns here instead of doing it with every win check.
    def __init__(self, bingoboard):
        self.bingoboard = bingoboard

    def Mark(self, mark):  # Mark a called bingo spot with -1
        mark = int(mark)  # I should probably do this at the parse.
        for x in self.bingoboard:  # There's a better way to find/ replace a list item. There has to be.
            pos = 0
            for y in x:
                if y == mark:
                    x[pos] = -1
                else:
                    pos += 1

    def Winning(self, number):
        columns = [[], [], [], [], []]  # Again, there has to be a way to have done this dynamically.
        for x in self.bingoboard:
            if sum(x) == -5:  # Check rows for winners
                score = Scoring(self.bingoboard, number)
                return "won", score
        count = 0
        for y in range(0, len(self.bingoboard[0])):  # Create list of columns
            for x in self.bingoboard:
                columns[y].append(x[count])
            count += 1
        for x in columns:  # Check columns for winners
            if sum(x) == -5:
                score = Scoring(self.bingoboard, number)
                return "won", score


def Scoring(boards, number):
    scoresum = []
    for x in boards:
        for y in x:
            if y > 0:
                scoresum.append(y)
    return sum(scoresum) * int(number)


def BoardMaker(boards):
    boardtomake = []
    for x in boards[0:5]:
        x = x.split(" ")
        while '' in x:
            x.remove('')
        boardtomake.append([int(y) for y in x])
    del boards[0:5]
    return board(boardtomake)


draws = bingo[0].split(",")  # There ought to be a way to make them ints here.
bingo.pop(0)
boards = []
winners = []
while len(bingo) > 1:
    boards.append(BoardMaker(bingo))  # Make board objects
for x in draws:
    for y in boards:  # Mark all boards
        y.Mark(x)
    for y in boards:  # Check boards for winners
        z = y.Winning(x)

        if (type(z)) == tuple:
            if "won" in z:  # I suppose this is redundant. It won if it returned a tuple.
                if len(winners) == 0:
                    print("First winner scores:  " + str(z[1]))
                if len(winners) == 99:
                    print("The last winner scores: " + str(z[1]))
                winners.append(y)
                boards.remove(y)
    if len(winners) == 100:  # Stops when everything has won
        break
