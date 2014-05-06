##Brian Chesley TicTacToe
import random
import collections

def display_board(board):
    print
    print " ".join(board)

def other_player(turn):
    return 3-turn
    
def player_move(board,turn):
    row = int(raw_input("what row would you like player %s? " % (turn,)))
    column = int(raw_input("what column would you like player %s? " % (turn,)))
    while not (1 <= row <= 3 and 1 <= column <= 3)\
    or board[row-1][column-1] != "":
        row = int(raw_input\
        ("That coordinate is not available. What row would you like player %s? " % (turn,)))
        column = int(raw_input("what column would you like player %s? " % (turn,)))
    return (row-1, column-1)

def game_type():
    choice = raw_input("Hello! Would you like to play against the Computer? Click 1 for yes. ")
    if choice == str(1):
        return True

def random_selection():
    numchoice = input("Choose a number 1 or 2 to go first ")
    number = random.randrange(1,3)
    if numchoice == number:
        print "You got it. Move first "
        return True
    else:
        print "Nope! Computer's move "
        return False

def make_move(board,turn,move):
    board[move[0]][move[1]] = turn

def main():
    """instead of having two separate loops I wanted to have an if statement that created
    player1 player 2 variables depending upon random selection, but every time I did this 
    I got an infinite loop that kept printing out the game board after 1 "correct" interation
    code below
    
    if random_selection():
        playerOne = player_move(board,turn)
        playerTwo = computer_AI(board,turn)
    else:
        playerTwo = player_move(board,turn)
        playerOne = computer_AI(board,turn)
    while True: ...
    
    or is there a way to make this work? Or better a way so I only need one loop (instead of two/three)?
    """
    
    board = [["","",""],["","",""],["","",""]]
    turn = 1
    display_board(board)
    if game_type():
        if random_selection():            
            while True:
                make_move(board,turn,player_move(board,turn))
                display_board(board)
                if is_winner(board,turn):
                    print "Player %s wins!! " % (turn)
                    return
                if tie(board):
                    print "Tie!"
                    return
                turn = other_player(turn)
                make_move(board, turn, computer_AI(board,turn))
                if is_winner(board,turn):
                    print "Player %s wins!! " % (turn)
                    return
                if tie(board):
                    print "Tie!"
                    return
                display_board(board)
                turn = other_player(turn)
        else:
            while True:
                make_move(board, turn, computer_AI(board,turn))
                display_board(board)
                if is_winner(board,turn):
                    print "Player %s wins!! " % (turn)
                    return
                if tie(board):
                    print "Tie!"
                    return
                turn = other_player(turn)
                make_move(board,turn,player_move(board,turn))
                display_board(board)
                if is_winner(board,turn):
                    print "Player %s wins!! " % (turn)
                    return
                if tie(board):
                    print "Tie! "
                    return
                turn = other_player(turn)
            
    else:
        while True:
            make_move(board,turn,player_move(board,turn))
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
        if board[0][e] == board[1][e] == board[2][e] == turn\
        or board[e][0] == board[e][1] == board [e][2] == turn\
        or board[0][0] == board[1][1] == board[2][2] == turn\
        or board[0][2] == board[1][1] == board[2][0] == turn:
            return True
    
def tie(board):
    count = 0
    for row in board:
        count += row.count("")
    if count == 0:
        return True
        
def two_of_three(board, turn):
    """
    I coded this up two different ways...Is there a reason to prefer one over the other?
    """
    
    gamelist = []
    row1 = board[0]
    row2 = board[1]
    row3 = board[2]
    columns = zip(*board)
    column1 = columns[0]
    column2 = columns[1]
    column3 = columns[2]
    d1 = [board[0][0], board[1][1], board[2][2]]
    d2 = [board[0][2], board[1][1], board[2][0]]
    wins = [row1, row2, row3, column1, column2, column3, d1, d2]
    winsPosition = 0

    for ways in wins:
        winsPosition = winsPosition + 1
        counter = collections.Counter(ways)
        if counter.get(turn) == 2 and counter.get("") == 1:
            gamelist.append(ways)
            gamelist.append(winsPosition-1)
    if gamelist:
        return gamelist
    else:
        return False
"""    
    for ways in wins:
        winsPosition = winsPosition + 1
        count = 0
        blankcount = 0
        for way in ways:
            if way == turn:
                count = count + 1
            if way == "":
                blankcount = blankcount + 1
            if count == 2 and blankcount == 1:
                gamelist.append(ways)
                gamelist.append(winsPosition-1)
    if len(gamelist) > 0:
        return gamelist
    else:
        return False
"""
def AImove(gamelist):
    """
    for some reason the statements like this: if 3 >= gamelist[1] >= 5: didn't work for me
    What am I missing here?
    
    """
    if gamelist[1] == 5 or gamelist[1] == 4 or gamelist[1] == 3:
        return [gamelist[0].index(""), gamelist[1]-3]
        
    elif gamelist[1] == 0 or gamelist[1] == 1 or gamelist[1] == 2:
        return [gamelist[1], gamelist[0].index("")]
    
    elif gamelist[1] == 6:
        return [gamelist[0].index(""), gamelist[0].index("")]
    
    elif gamelist[1] == 7:
        return [gamelist[0].index(""), 2 - gamelist[0].index("")]
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
                value = turn
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
