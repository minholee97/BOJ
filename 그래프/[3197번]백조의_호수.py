# https://www.acmicpc.net/problem/3197

import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
result = 0
flag = 0
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
lake = []
visited = [[0] * C for _ in range(R)]
w_visited = [[0] * C for _ in range(R)]
swan = []
wq = deque()
nwq = deque()
for i in range(R):
	lake.append(list(sys.stdin.readline().rstrip()))
	for j in range(C):
		if lake[i][j] == '.':
			wq.append([i, j])
		elif lake[i][j] == 'L':
			swan.append([i, j])
			wq.append([i, j])
q = deque()
nq= deque()
q.append(swan[0])
while True:
	while len(q) != 0:
		cur = q.popleft()
		for i in range(4):
			x = cur[0] + move[i][0]
			y = cur[1] + move[i][1]
			if 0 <= x < R and 0 <= y < C:
				if lake[x][y] == 'X' and visited[x][y] == 0:
					nq.append([x, y])
					visited[x][y] = 1
				elif lake[x][y] != 'X' and visited[x][y] == 0:
					if [x, y] == swan[1]:
						flag = 1
						break
					q.append([x, y])
					visited[x][y] = 1
		if flag == 1:
			break
	if flag == 1:
		break
	while len(wq) != 0:
		cur = wq.popleft()
		for i in range(4):
			x = cur[0] + move[i][0]
			y = cur[1] + move[i][1]
			if 0 <= x < R and 0 <= y < C:
				if lake[x][y] == 'X' and w_visited[x][y] == 0:
					lake[x][y] = '.'
					w_visited[x][y] = 1
					nwq.append([x, y])
				elif lake[x][y] != 'X' and w_visited[x][y] == 0:
					wq.append([x, y])
					w_visited[x][y] = 1
	q = nq
	wq = nwq
	nq = deque()
	nwq = deque()
	result += 1
print(result)