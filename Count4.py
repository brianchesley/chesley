##Brian Chesley, Connect 4
import itertools

def display(board):
    for row in board:
        print row

def other_player(player):
    return 3 - player

def run():
    board = [[0]*7 for _ in range(6)]
    display(board)
    main_loop(board, 1)

def main_loop(board, turn):
    while True:
        make_move(board, turn, player_move(board, turn)) #makes moves
        display(board)
        if isWinner(board):
            print "Player %d wins!" % turn
            return
        if tie(board):
            print "Tie Game!"
            return
        turn = other_player(turn)

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
    if horizontal_win(board) or vertical_win(board) or diagonal_win(board):
        return True
    return False

def horizontal_win(board):
    for row in board: ##check to find a horizontal win
        last = -10
        for value in row:
            if value != last:
                last = value
                length = 1
            else:
                length = length + 1
            if length == 4:
                if value in [1, 2]:
                    return True

def vertical_win(board):
    columns = zip(*board)
    for player in [1, 2]:
        for column in columns:
            if [player for player, run in itertools.groupby(column)
                       if len(list(run)) >= 4 and player in [1, 2]]:
                return True

def diagonal_win(board):
    ways = []
    for row in range(0, 3): ## check for a diagonal win. \
        for column in range(0, 4):
            ways.append([(row+i, column+i) for i in range(4)])
    for row in range(3, 6): ## check for a diagonal win. /
        for column in range(0, 4):
            ways.append([(row-i, column+i) for i in range(4)])
    for way in ways:
        values = [board[way[i][0]][way[i][1]] for i in range(4)]
        if values[1:] == values[:-1] and values[0] in [1, 2]:
            return True

def tie(board):
    return all(all(row) for row in board)

run()
