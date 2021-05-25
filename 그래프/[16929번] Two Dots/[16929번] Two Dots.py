import sys
from collections import deque

mv = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dfs(d, p, c):
	for i in range(4):
		x = d[0] + mv[i][0]
		y = d[1] + mv[i][1]
		if 0 <= x < N and 0 <= y < M and mv[i] != p and bd[x][y] == c:
			if st == [x, y]:
				print("Yes")
				exit()
			if visited[x][y] == False:
				visited[x][y] = True
				dfs([x, y], [-mv[i][0], -mv[i][1]], c)
				visited[x][y] = False

N, M = map(int, sys.stdin.readline().split())

bd = []

for _ in range(N):
	line = list(sys.stdin.readline().rstrip())
	bd.append(line)

for i in range(N):
	for j in range(M):
		st = [i, j]
		visited = [[False for _ in range(M)] for _ in range(N)]
		visited[i][j] = True
		dfs([i, j], None, bd[i][j])
print("No")