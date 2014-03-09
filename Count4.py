##Brian Chesley, Connect 4

def tie():		
	for row in range(6):
		for column in range(6):
			if board[row][column] == 0:
				return False
	return True		

def run():
	board = []
	for i in range(0,6):
		board.append([0]*7)
	for row in board:
		print row
	turn = 1
	p1_wins = False
	p2_wins = False
	
	
	while p1_wins != True and p2_wins != True: #players input moves
		
				
		if turn == 1:
			while True:
				try:
					p1_column = input("what column would you like player 1? ")
					while not (1 <= p1_column <= 7):
						p1_column = input("Please enter a valid column # between 1 and 7 ")
					while board[0][p1_column -1] != 0:
						p1_column = input("This column is full. Enter a different one ")
					break
				except NameError: ##Still fails when user uses space
					print "Please enter a valid column # between 1 and 7  "
			for row in reversed(range(0,6)):
				if board[row][p1_column-1] == 0:
					board[row][p1_column-1] = 1
					break
				else:
					pass
		else:
			while True:
				try:
					p1_column = input("what column would you like player 2? ")
					while not (1 <= p1_column <= 7):
						p1_column = input("Please enter a valid column # between 1 and 7  ")
					break
				except NameError:
					print "Please enter a valid column # between 1 and 7  "
			for row in reversed(range(0,6)):
				if board[row][p1_column-1] == 0:
					board[row][p1_column-1] = 2
					break
				else:
					pass
		if tie == True: #handles a tie game
				print "Tie Game!"
				p1_wins = True	
		
		if isWinner(board) == True:
			if turn == 1:
				print "player 1 wins!"
				p1_wins = True
			else:
				print "player 2 wins!"
				p2_wins = True
			
		
		if turn == 1: ##switches turn
			turn = 2
		else:
			turn = 1
	
		for row in board: ##prints board
			print row

def isWinner(board):
	row_check = -1
	new_row = None
	last = -10
	for row in range(0,6): ##check to find a horizontal win
		for column in range(0,7):
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
	for column in range(0,7): ##check for a win vertically
		for row in range(0,6):
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
		for row in range(0,4): ## check for a diagonal win. \
			for column in range(0,4):
				if board[row][column] == board[row+1][column+1] == board[row+2][column+2] == board[row+3][column+3]:
					if board[row][column] == 1:
						return True
					elif board[row][column] == 2:
						return True
			
		for row in range(3,6): ## check for a diagonal win. /
			for column in range(0,4):		
				if board[row][column] == board[row-1][column+1] == board[row-2][column+2] == board[row-3][column+3]:
					if board[row][column] == 1:
						return True
					elif board[row][column] == 2:
						return True
	except IndexError:
		pass
		


print run()

