import pprint

def checkRow(rowIndex, startPos, playerNum):
    length = len(rowIndex)
    isFive = 0
    for x in range(19):
        if (x + startPos) < length:
            print rowIndex[x + startPos]
            if (rowIndex[x + startPos] == playerNum):
                isFive += 1
            else:
                break
        else: 
            break
    countdown = 1
    while countdown <= 4:
        if startPos - countdown >= 0:
            if (rowIndex[startPos - countdown] == playerNum):
                isFive += 1
                countdown += 1
            else:
                break
        else:
            break
    return (isFive >= 5)

def checkColumn(board, row, column, playerNum):
    length = len(board[0])
    isFive = 0
    countdown = row
    while countdown >= 0:
        if (board[countdown][column] == playerNum):
            isFive += 1
            countdown -= 1
        else:
            break
    countdown = row + 1
    while countdown != length:
        if (board[countdown][column] == playerNum):
            isFive += 1
            countdown += 1
        else:
            break
    return (isFive >= 5)

def checkDiagDec(board, row, column, playerNum):
    length = len(board[0])
    isFive = 0
    countdownRow = row
    countdownCol = column
    while countdownRow >= 0 and countdownCol >= 0:
        if (board[countdownRow][countdownCol] == playerNum):
            isFive += 1
            countdownRow -= 1
            countdownCol -= 1
        else:
            break
    countdownRow = row + 1
    countdownCol = column + 1
    while countdownRow < length and countdownCol < length:
        if (board[countdownRow][countdownCol] == playerNum):
            isFive += 1
            countdownRow += 1
            countdownCol += 1
        else:
            break
    return (isFive >= 5)

def checkDiagInc(board, row, column, playerNum):
    length = len(board[0])
    isFive = 0
    countdownRow = row
    countdownCol = column
    while countdownRow >= 0 and countdownCol != length:
        if (board[countdownRow][countdownCol] == playerNum):
            isFive += 1
            countdownRow -= 1
            countdownCol += 1
        else:
            break
    countdownRow = row + 1
    countdownCol = column - 1
    while countdownCol >= 0 and countdownRow != length:
        if (board[countdownRow][countdownCol] == playerNum):
            isFive += 1
            countdownRow += 1
            countdownCol -= 1
        else:
            break
    return (isFive >= 5)

# checks if any player has won the game
def isWinner(board, row, column):
    playerNum = board[row][column]

    isRowFive = checkRow(board[row], column, playerNum)
    isColumnFive = checkColumn(board, row, column, playerNum)
    isDiagDecFive = checkDiagDec(board, row, column, playerNum)
    isDiagIncFive = checkDiagInc(board, row, column, playerNum)

    return isRowFive or isColumnFive or isDiagDecFive or isDiagIncFive is True

def placeItem(row, column, board, current_player):
    if board[row][column] != "| |":
        print "This space is already taken. Please enter new coordinates"
        return False
    else:
        board[row][column] = "|%s|" % current_player
        return True

def getLocation():
    location = raw_input("Enter two numbers seperated by a comma, like y-coordinate,x-coordinate ")
    coordinates = map(int, location.split(','))

    while (len(coordinates) != 2 or coordinates[0] < 0 or coordinates[0] >= 19 or coordinates[1] < 0 or coordinates[1] >= 19):
        print "You inputted a location in an invalid format"
        location = raw_input("Enter two numbers seperated by a comma, like y-coordinate,x-coordinate ")
        coordinates = map(int, location.split(','))
    return coordinates

def main():
    num_moves = 0
    #pp = pprint.PrettyPrinter()
    isWon = False
    current_player = 1
    prev_player = 2
    board = [["| |" for x in range(19)] for x in range(19)]

    while (isWon == False):
        print "---------------------------------------"
        print "This is the current board: "

        for x in range(19):
            print ''.join(map(str, board[x]))

        coordinates = getLocation()
        if (placeItem(coordinates[0], coordinates[1], board, current_player)):
            temp = current_player
            current_player = prev_player
            prev_player = temp

            isWon = True if isWinner(board, coordinates[0], coordinates[1]) else False
            num_moves += 1

        if num_moves == (19 * 19):
            print "There is no winner, the game is over!"
            break

    if isWon:
        print "---------------------------------------"
        print "This is the current board: "
        for x in range(19):
            print ''.join(map(str, board[x]))
        print "%s won!" % prev_player

main()