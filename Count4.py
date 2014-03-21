##Brian Chesley, Connect 4

def display(board):
    for row in board:
        print row

def other_player(player):
    return 3 - player

def run():
    board = [[0]*7 for _ in range(6)]
    display(board)
    turn = 1

    while True:      #main game loop
        make_move(board, turn, player_move(board, turn)) #makes moves

        if isWinner(board): #checks for winner
            print "Player %d wins!" % turn
            return

        if tie(board): #handles a tie game
            print "Tie Game!"

        turn = other_player(turn)

        display(board)

def player_move(board, turn):
    while True:
        try:
            player_column = int(raw_input( "what column would you like player %d? " % (turn,)))
        except ValueError:
            print "Please enter a valid column # between 1 and 7"
        else:
            if not (1 <= player_column <= 7):
                print "Please enter a valid column # between 1 and 7"
            elif board[0][player_column -1] != 0:
                print "This column is full. Enter a different one"
            else:
                return player_column

def make_move(board, turn, move):
    for row in reversed(range(0, 6)):
        if board[row][move-1] == 0:
            board[row][move-1] = turn
            break

def isWinner(board):
    last = -10
    for row in range(0, 6): ##check to find a horizontal win
        for column in range(0, 7):
            if board[row][column] != last or row == 0:
                last = board[row][column]
                length = 1
            else:
                length = length + 1
            if length == 4:
                if board[row][column] == 1:
                    return True
                elif board[row][column] == 2:
                    return True
    col_check = -1
    new_column = None
    for column in range(0, 7): ##check for a win vertically
        for row in range(0, 6):
            if column != col_check: ##to make sure columns don't carry over
                col_check = column
                new_column = True
            else:
                new_column = False
            if board[row][column] != last or new_column:
                last = board[row][column]
                length = 1
            elif board[row][column] == last and not new_column:
                length = length + 1
            if length == 4:
                if board[row][column] == 1:
                    return True
                elif board[row][column] == 2:
                    return True
    try:
        for row in range(0, 4): ## check for a diagonal win. \
            for column in range(0, 4):
                if board[row][column] == board[row+1][column+1] == board[row+2][column+2] == board[row+3][column+3]:
                    if board[row][column] == 1:
                        return True
                    elif board[row][column] == 2:
                        return True

        for row in range(3, 6): ## check for a diagonal win. /
            for column in range(0, 4):
                if board[row][column] == board[row-1][column+1] == board[row-2][column+2] == board[row-3][column+3]:
                    if board[row][column] == 1:
                        return True
                    elif board[row][column] == 2:
                        return True
    except IndexError:
        pass

def tie(board):
    for row in range(6):
        for column in range(7):
            if board[row][column] == 0:
                return False
    return True

run()
