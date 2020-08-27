board = [
	[7, 8, 0, 4, 0, 0, 1, 2, 0],
	[6, 0, 0, 0, 7, 5, 0, 0, 9],
	[0, 0, 0, 6, 0, 1, 0, 7, 8],
	[0, 0, 7, 0, 4, 0, 2, 6, 0],
	[0, 0, 1, 0, 5, 0, 9, 3, 0],
	[9, 0, 4, 0, 6, 0, 0, 0, 5],
	[0, 7, 0, 3, 0, 0, 0, 1, 2],
	[1, 2, 0, 0, 0, 7, 4, 0, 0],
	[0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(boa):
	find = find_empty(boa)
	if not find:
		return True
	else:
		row, col = find
	for i in range(1, 10):
		if valid(boa, i, (row, col)):
			boa[row][col] = i

			if solve(boa):
				return True

			boa[row][col] = 0
	return False


def valid(bo, num, pos):
	# check row:
	for i in range(len(bo[0])):
		if bo[pos[0]][i] == num and i != pos[1]:
			return False
	# check column:
	for j in range(len(bo[0])):
		if bo[j][pos[1]] == num and j != pos[0]:
			return False
	# check box:
	x_box = pos[0] // 3
	y_box = pos[1] // 3
	for i in range(x_box * 3, x_box * 3 + 3):
		for j in range(y_box * 3, y_box * 3 + 3):
			if bo[i][j] == num and (i, j) != pos:
				return False
	return True


def print_board(bo):
	for i in range(len(bo[0])):
		if i % 3 == 0 and i != 0:
			print('---------------------')
		for j in range(len(bo[0])):
			if j % 3 == 0 and j != 0:
				print(' | ', end="")
			if j == 8:
				print(bo[i][j])
			else:
				print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
	for i in range(len(bo)):
		for j in range(len(bo)):
			if bo[i][j] == 0:
				return (i, j)

	return None


print_board(board)
solve(board)
print("___________________")
print_board(board)
