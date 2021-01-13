# https://www.acmicpc.net/problem/2178

import sys
from collections import deque

move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N, M = map(int, sys.stdin.readline().split())
maze = []
visited = [[0] * M for _ in range(N)]
for _ in range(N):
	maze.append(sys.stdin.readline().rstrip())
q = deque()
q.append([0, 0, 1])
while len(q) != 0:
	cur = q.popleft()
	if cur[0] == N - 1 and cur[1] == M - 1:
		print(cur[2])
	for i in range(4):
		x = cur[0] + move[i][0]
		y = cur[1] + move[i][1]
		if 0 <= x < N and 0 <= y < M:
			if visited[x][y] == 0 and maze[x][y] == '1':
				visited[x][y] = 1
				q.append([x, y, cur[2] + 1])