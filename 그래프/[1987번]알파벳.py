# https://www.acmicpc.net/problem/1987
# pypy3로 채점... (python3 시간초과)

import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
board = []
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
result = 1
for _ in range(R):
	board.append(list(sys.stdin.readline().rstrip()))
q = deque()
q.append([0, 0, board[0][0]])
while True:
	if len(q) == 0:
		break
	cur = q.pop()
	for i in range(4):
		x = cur[0] + move[i][0]
		y = cur[1] + move[i][1]
		if 0 <= x < R and 0 <= y < C:
			if cur[2].find(board[x][y]) == -1:
				s = cur[2] + board[x][y]
				q.append([x, y, s])
				if len(s) > result:
					result = len(s)
print(result)