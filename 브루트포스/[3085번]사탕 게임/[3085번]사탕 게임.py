import sys
from collections import deque

def check():
	candy = 0
	for i in range(N):
		r_count = 1
		c_count = 1
		for j in range(N - 1):
			if board[i][j] == board[i][j + 1]:
				r_count += 1
			else:
				candy = max(r_count, candy)
				r_count = 1
			if board[j][i] == board[j + 1][i]:
				c_count += 1
			else:
				candy = max(c_count, candy)
				c_count = 1
		candy = max(r_count, candy)		
		candy = max(c_count, candy)
	return candy

N = int(sys.stdin.readline().rstrip())
board = []
for _ in range(N):
	board.append(list(sys.stdin.readline().rstrip()))

maximum = 0
for i in range(N):
	for j in range(N - 1):
		board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
		maximum = max(maximum, check())
		board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

		board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]
		maximum = max(maximum, check())
		board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]

print(maximum)
