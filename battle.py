import colors
guess_row = 0
guess_col = 0
gotOne = 0
hitCol = 0
hitRow = 0
board = []
guess_rowHum = 0
guess_colHum = 0
gotOneHum = 0
hitColHum = 0
hitRowHum = 0
boardHum = []
variPos = 0
from random import randint
import time
size = 9
for x in range(size):
    board.append(["~"] * size)
    boardHum.append(["~"] * size)

def print_board(b):
    n = 1
    colval = "  "
    while n <= size:
        colval = colval + str(n) + " "
        n = n + 1
    print colval
    n = 1
    for row in b:
        print str(n) + " " + " ".join(row)
        n = n + 1

print "This is the board:"
print
print_board(board)
print
print

vhq = raw_input("Would you like your ship to be Verticle or Horizontal (Type V or H): ")
while vhq != "V" and vhq != "v" and vhq != "H" and vhq != "h":
    vhq = raw_input("Would you like your ship to be Verticle or Horizontal (Type V or H): ")
vh = vhq.upper()
while variPos == 0:
    if vh == "V":
        posRow = raw_input("In which row would you like to place the top of your ship (Between 1 and " + str(size - 1) + "): ")
        posCol = raw_input("In which column would you like to place your ship (Between 1 and " + str(size) + "): ")
        variPos = 1
    elif vh == "H":
        posRow = raw_input("In which row would you like to place your ship (Between 1 and " + str(size) + "): ")
        posCol = raw_input("In which column would you like to place the left side your ship (Between 1 and " + str(size - 1) + "): ")
        variPos = 1
    else:
        with colors.pretty_output(colors.BOLD, colors.FG_RED) as out:
            out.write("You didn't type V or H!")
        variPos = 0
ship_row = int(posRow) - 1
ship_col = int(posCol) - 1
if vh == "V":
    pship_row = ship_row + 1
    pship_col = ship_col
else:
    pship_row = ship_row
    pship_col = ship_col + 1
def guessCol(min, max):
    return randint(min, max)
def guessRow(min, max):
    return randint(min, max)
print
print
print "Your guesses:"
print_board(boardHum)
print
print "My guesses:"
print_board(board)

def horizontal():
    return randint(0, 1)

if horizontal() == 0:
    ship_rowHum = randint(0, len(boardHum) - 2)
    ship_colHum = randint(0, len(boardHum) - 1)
    pship_rowHum = ship_rowHum + 1
    pship_colHum = ship_colHum
else:
    ship_rowHum = randint(0, len(boardHum) - 1)
    ship_colHum = randint(0, len(boardHum) - 2)
    pship_rowHum = ship_rowHum
    pship_colHum = ship_colHum + 1

for turn in range(999):
    throw = str(turn + 1)
    print
    print "Turn " + throw + ":"

    if gotOne == 0:
        guess_col = guessCol(0, size - 1)
        guess_row = guessRow(0, size - 1)
        while board[guess_row][guess_col] != "~":
            guess_col = guessCol(0, size - 1)
            guess_row = guessRow(0, size - 1)
    else:
        guessDir = randint(0, 3)
        if guessDir == 0:
            guess_col = hitCol
            guess_row = hitRow - 1
            if guess_row < 0: guess_row = 0
        if guessDir == 1:
            guess_col = hitCol + 1
            guess_row = hitRow
            if guess_col > (size - 1): guess_col = (size - 1)
        if guessDir == 2:
            guess_col = hitCol
            guess_row = hitRow + 1
            if guess_row > (size - 1): guess_row = (size - 1)
        if guessDir == 3:
            guess_col = hitCol - 1
            guess_row = hitRow
            if guess_col < 0: guess_col = 0
        while board[guess_row][guess_col] != "~":
            guessDir = randint(0, 3)
            if guessDir == 0:
                guess_col = hitCol
                guess_row = hitRow - 1
                if guess_row < 0: guess_row = 0
            if guessDir == 1:
                guess_col = hitCol + 1
                guess_row = hitRow
                if guess_col > (size - 1): guess_col = (size - 1)
            if guessDir == 2:
                guess_col = hitCol
                guess_row = hitRow + 1
                if guess_row > (size - 1): guess_row = (size - 1)
            if guessDir == 3:
                guess_col = hitCol - 1
                guess_row = hitRow
                if guess_col < 0: guess_col = 0

    grow = raw_input("In which row would you like to guess: ")
    gcol = raw_input("In which column would you like to guess: ")
    if grow.isdigit():
        grow = grow
    else:
        grow = 9
    if gcol.isdigit():
        gcol = gcol
    else:
        gcol = 9
    ggrow = int(grow)
    ggcol = int(gcol)
    if ggrow >= 10:
        ggrow = 9
    if ggcol >= 10:
        ggcol = 9
    if ggrow <= 0:
        ggrow = 1
    if ggcol <= 0:
        ggcol = 1
    guess_rowHum = ggrow - 1
    guess_colHum = ggcol - 1

    if (boardHum[guess_rowHum][guess_colHum] != "~"):
        print
        print '\033[31m' + "--You guessed that one already, idiot!--" + '\033[0m'
    elif (guess_rowHum == ship_rowHum and guess_colHum == ship_colHum) or (guess_rowHum == pship_rowHum and guess_colHum == pship_colHum):
        if gotOneHum == 0:
            gotOneHum = 1
            boardHum[guess_rowHum][guess_colHum] = '\033[32m' + '\033[1m' + "H"  + '\033[0m'
            print
            print '\033[32m' + "--You hit my battleship!--" + '\033[0m'
            hitColHum = guess_colHum
            hitRowHum = guess_rowHum
        else:
            gotOne = 2
            boardHum[guess_rowHum][guess_colHum] = '\033[32m' + '\033[1m' + "W" + '\033[0m'
            print
            print '\033[32m' + "--You sank my battleship on turn " + throw + "!--" + '\033[0m'
    else:
        boardHum[guess_rowHum][guess_colHum] = '\033[31m' + '\033[1m' + "X" + '\033[0m'
        print
        print '\033[31m' + "--You missed my battleship!--" + '\033[0m'

    if (board[guess_row][guess_col] != "~"):
        print
        print '\033[31m' + "--I guessed that one already, idiot that I am!--" + '\033[0m'
        print
    elif (guess_row == ship_row and guess_col == ship_col) or (guess_row == pship_row and guess_col == pship_col):
        if gotOne == 0:
            gotOne = 1
            board[guess_row][guess_col] = '\033[32m' + '\033[1m' + "H" + '\033[0m'
            print
            print '\033[32m' + "--I hit your battleship!--" + '\033[0m'
            hitCol = guess_col
            hitRow = guess_row
        else:
            gotOne = 2
            board[guess_row][guess_col] = '\033[32m' + '\033[1m' + "W" + '\033[0m'
            print
            print '\033[32m' + "--I sank your battleship on turn " + throw + "!--" + '\033[0m'
            print '\033[32m' + "--My ship was located at: Row: " + str(ship_row) + " and Column: " + str(ship_col) + "!--" + '\033[0m'
    else:
        board[guess_row][guess_col] = '\033[31m' + '\033[1m' + "X" + '\033[0m'
        print
        print '\033[31m' + "--I missed your battleship!--" + '\033[0m'
      
    print "Your guesses:"
    print_board(boardHum)
    print
    print "My guesses:"
    print_board(board)

    if gotOne == 2: break
