##Brian Chesley TicTacToe
import random
import collections

def display_board(board):
    print
    print "\n-----\n".join("|".join(str(x) if x else ' ' for x in row) for row in board)

def other_player(turn):
    return 3 - turn

def player_move(board,turn):
    row = int(raw_input("What row would you like player %s? " % (turn,)))
    column = int(raw_input("What column would you like player %s? " % (turn,)))
    while (not (1 <= row <= 3 and 1 <= column <= 3)
        or board[row-1][column-1] != ""):
        row = int(raw_input("That coordinate is not available."
                            "What row would you like player %s? " % (turn,)))
        column = int(raw_input("What column would you like player %s? " % (turn,)))
    return (row-1, column-1)

def game_type():
    choice = raw_input("Hello! Would you like to play against the Computer? Type 1 for yes. ")
    if choice == str(1):
        return True

def random_selection():
    input("Choose a number 1 or 2 to go first ")
    if random.randrange(0,2):
        print "You got it. Move first "
        return True
    else:
        print "Nope! Computer's move "
        return False

def make_move(board,turn,move):
    board[move[0]][move[1]] = turn

def main():
    board = [["","",""],["","",""],["","",""]]
    turn = 1
    display_board(board)
    if game_type:
        players = (player_move, computer_AI) if random_selection() else (computer_AI, player_move)
    else:
        players = player_move, player_move

    while True:

        #turns are 1-indexed, while the players array is 0-indexed
        make_move(board, turn, players[turn-1](board,turn))

        display_board(board)
        if is_winner(board,turn):
            print "Player %s wins!! " % (turn)
            return
        if tie(board):
            print "Tie!"
            return
        turn = other_player(turn)

def is_winner(board,turn):
    for e in range(0,3):
        if (board[0][e] == board[1][e] == board[2][e] == turn
            or board[e][0] == board[e][1] == board[e][2] == turn):
            return True
    if (board[0][0] == board[1][1] == board[2][2] == turn
        or board[0][2] == board[1][1] == board[2][0] == turn):
        return True

def tie(board):
    count = 0
    for row in board:
        count += row.count("")
    if count == 0:
        return True

def two_of_three(board, turn):
    """
    Return list of spots for which one move would win
    """

    gamelist = []
    row_ways = [zip(row, range(3)) for row in range(3)]
    column_ways = zip(*row_ways)
    d1 = [(0, 0), (1, 1), (2, 2)]
    d2 = [(0, 2), (1, 1), (2, 0)]
    wins = row_ways + column_ways + [d1, d2]

    for way in wins:
        values = [board[spot[0]][spot[1]] for spot in way]
        counter = collections.Counter(values)
        if counter[turn] == 2 and counter[""] == 1:
            gamelist.append(way[values.index("")])
    return gamelist

def AImove(gamelist):
    if gamelist:
        return gamelist[0]
    else:
        return False

def look_ahead(board,turn):
    """
    checks moves one ahead for double way win

    I initially wanted to have the list reset to the actual board after each iteration,
    but this didn't work hence the last line in the loop.

    I also tried not to index like we talked about, but I couldn't get the code to work. Any suggestions?


    look_ahead_list = list(board)
    move = []
    for row in board:
        for value in row:
            if value == "":
                value = turn  # this line right here doesn't do what it looks like you thought it did -
                              # have you worked with other languages before Python? It looks like you're
                              # expecting code like
                              x = [1, 2, 3]
                              a = x[0]
                              a = 4
                              # to produce
                              print x
                              # [4, 2, 3]

                              # but this is absolutely *not* how Python works.
                              # similarly,
                              for value in [1,2,3]:
                                  value = 10
                              # does *not* change the original list! It just changes what the name 'value' refers to.


                if two_of_three(look_ahead_list,turn) != False:
                    if len(two_of_three(look_ahead_list,turn)) > 3: 
                        move.append(row)
                        move.append(value)
                value = ""
    if len(move) > 0:
        return move
    else:
        return False
    """

    look_ahead_list = list(board)
    move = []
    for row in range(3):
        for value in range(3):
            if look_ahead_list[row][value] == "":
                look_ahead_list[row][value] = turn
                if two_of_three(look_ahead_list,turn) != False:
                    if len(two_of_three(look_ahead_list,turn)) > 3: 
                        move.append(row)
                        move.append(value)
                look_ahead_list[row][value] = ""
    if len(move) > 0:
        return move
    else:
        return False

def computer_AI(board,turn):
    center = [1,1]
    if two_of_three(board, turn) != False:
        return AImove(two_of_three(board, turn))
    elif two_of_three(board, 3-turn) != False:
        return AImove(two_of_three(board, 3-turn))
    elif board[1][1] == "":
        return center
    elif look_ahead(board,turn):
        return look_ahead(board,turn)
    elif look_ahead(board, 3-turn):
        return look_ahead(board, 3-turn)
    else:
        for i in range(3):
            for e in range(3):
                move = [i,e]
                while board[move[0]][move[1]] == "":
                    return move

main()
