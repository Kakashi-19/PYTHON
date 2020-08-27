board = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0]
]


def solve(bo, row):
	if row >= 4:
		return True

	for i in range(len(bo)):

		if valid(bo, (row, i)):
			bo[row][i] = 1

			if solve(bo, row + 1):
				return True

			bo[row][i] = 0

	return False


def print_board(bo):
	for i in range(len(bo)):
		if i != 0:
			print('- - - - - - - - - -')
		for j in range(len(bo)):
			if j == 3:
				print(bo[i][j])
			else:
				print(bo[i][j], end='  |  ')


def valid(bo, pos):
	# for i in range(len(bo)):
	# 	if bo[pos[0]][i] == 1 and i != pos[1]:
	# 		return False
	for j in range(len(bo)):
		if bo[j][pos[1]] == 1 and j != pos[0]:
			return False
	for i in range(len(bo)):
		for j in range(len(bo)):
			if i + j == pos[0] + pos[1] and (i, j) != pos:
				if bo[i][j] == 1:
					return False
	for i in range(len(bo)):
		for j in range(len(bo)):
			if i - j == pos[0] - pos[1] and (i, j) != pos:
				if bo[i][j] == 1:
					return False
	return True


print_board(board)
solve(board, 0)
print("Solving ...")
print("Solution Found!")

print_board(board)
