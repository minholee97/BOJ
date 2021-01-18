# https://www.acmicpc.net/problem/2468

import sys
from collections import deque

move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N = int(sys.stdin.readline().rstrip())
area = []
heights = [100, 1]
result = 0

def bfs(visited, cur, h):
	q = deque()
	q.append(cur)
	while len(q) != 0:
		c = q.popleft()
		for i in range(4):
			x = c[0] + move[i][0]
			y = c[1] + move[i][1]
			if 0 <= x < N and 0 <= y < N:
				if area[x][y] > h and visited[x][y] == 0:
					q.append([x, y])
					visited[x][y] = 1

for i in range(N):
	area.append(list(map(int, sys.stdin.readline().split())))
	if heights[0] > min(area[i]):
		heights[0] = min(area[i])
	if heights[1] < max(area[i]):
		heights[1] = max(area[i])

for i in range(heights[0] - 1, heights[1]):
	visited = [[0] * N for _ in range(N)]
	safety_zone = 0
	for j in range(N):
		for k in range(N):
			if area[j][k] > i and visited[j][k] == 0:
				visited[j][k] = 1
				bfs(visited, [j, k], i)
				safety_zone += 1
	if result < safety_zone:
		result = safety_zone
print(result)