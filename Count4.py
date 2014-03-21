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
    p1_wins = False
    p2_wins = False

    while not (p1_wins or p2_wins):      #main game loop
        make_move(board, turn, player_move(board, turn)) #makes moves

        if isWinner(board) == True: #checks for winner
            if turn == 1:
                print "Player 1 wins!"
                p1_wins = True
            else:
                print "Player 2 wins!"
                p2_wins = True

        if tie(board) == True: #handles a tie game
            print "Tie Game!"
            p1_wins = True

        turn = other_player(turn)

        for row in board: ##prints board
            print row


def player_move(board, turn):
    try:
        player_column = input("what column would you like player %d? " % (turn))
        while not (1 <= player_column <= 7):
            player_column = input("Please enter a valid column # between 1 and 7 ")
        while board[0][player_column -1] != 0:
            player_column = input("This column is full. Enter a different one ")
            break
    except NameError: ##Still fails when user inputs a space
        print "Please enter a valid column # between 1 and 7  "
    return player_column

def make_move(board, turn, move):
    for row in reversed(range(0, 6)):
        if board[row][move-1] == 0:
            if turn == 1:
                board[row][move-1] = 1
                break
            else:
                board[row][move-1] = 2
                break
        else:
            pass

def isWinner(board):
    row_check = -1
    new_row = None
    last = -10
    for row in range(0, 6): ##check to find a horizontal win
        for column in range(0, 7):
            if row != row_check:
                row_check = row
                new_row = True
            else:
                new_row = False
            if board[row][column] != last or new_row == True:
                last = board[row][column]
                length = 1
            else:
                length = length + 1
            if length == 4:
                if board[row][column] == 1:
                    return True
                elif board[row][column] == 2:
                    p2_wins = True
                    print "player 2 wins"
                    return p2_wins
    col_check = -1
    new_column = None
    for column in range(0, 7): ##check for a win vertically
        for row in range(0, 6):
            if column != col_check: ##to make sure columns don't carry over
                col_check = column
                new_column = True
            else:
                new_column = False
            if board[row][column] != last or new_column == True:
                last = board[row][column]
                length = 1
            elif board[row][column] == last and new_column == False:
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
