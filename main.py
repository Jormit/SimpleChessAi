import chess
import random
import chess.svg


board = chess.Board()

# Assign values to pieces.
values = {chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 0}

def random_move(board):
	# Get legal moves and place in list.
	legal_moves = []
	for i in board.legal_moves:
		legal_moves.append(i)

	board.push(random.choice(legal_moves))

# Randomly selects move with best valuation.
def best_move(board):
	best_moves = []

	max = -999

	# Loop through all the legal moves and store best moves.
	for i in board.legal_moves:
		# Do the move and store the board value.
		board.push(i)

		# Recursive tree valuator returns worst possible value.
		move_value = min(board,2) + get_board_value(board)

		# If the value is equal to the max value store move.
		if (move_value == max):
			best_moves.append(i)

		# If the move is greater then clear list of moves and store that move.
		elif (move_value > max):
			best_moves.clear()
			best_moves.append(i)
			max = move_value

		# Undo the move before trying next move.
		board.pop()

	# Randomly select from the list of best moves.
	board.push(random.choice(best_moves))

# Find min in tree.
def min(board,depth):
	worst = 999
	
	for i in board.legal_moves:
		# Do the move and store the board value.
		board.push(i)

		if (depth != 0):
			move_value = get_board_value(board) + max(board,depth - 1)
		else:
			board.pop()		
			return 0		

		if (move_value < worst):
			worst = move_value		
		
		# Go down to next level if max depth hasn't been reached
		board.pop()
		

	return worst

# Find max in tree.
def max(board,depth):
	max = -999
	
	for i in board.legal_moves:
		# Do the move and store the board value.
		board.push(i)

		if (depth != 0):
			move_value = get_board_value(board) + min(board,depth - 1)
		else:
			board.pop()		
			return 0		

		if (move_value > max):
			max = move_value		
		
		# Go down to next level if max depth hasn't been reached
		board.pop()
		

	return max

# Add up all the pieces on each side to get the value of blacks advantage.
def get_board_value(board):
	count = 0;
	pm = board.piece_map()
	for i in pm:
		val = values[pm[i].piece_type]

		if pm[i].color == chess.WHITE:
			count-=val

		if pm[i].color == chess.BLACK:
			count+=val

	return count;

# Main loop
while (board.is_game_over() == False):	
	
	while(1):
		try: 
			move = input()
			board.push_san(move)			
			break			
		except:
			if (move == "q"):
				exit(1)
			print("Invalid Move!")	

	print("------You------")
	print(board)		
	best_move(board)
	print("-------Ai------")
	print(board)
	