# https://www.acmicpc.net/problem/14502

import sys
import copy
from collections import deque

result = 0
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(c_lab):
	q = deque()
	safe = 0
	for i in range(len(virus)):
		q.append(virus[i])
	while len(q) != 0:
		cur = q.popleft()
		for i in range(4):
			x = cur[0] + move[i][0]
			y = cur[1] + move[i][1]
			if 0 <= x < N and 0 <= y < M:
				if c_lab[x][y] == '0':
					c_lab[x][y] = '2'
					q.append([x, y])
	for i in range(N):
		for j in range(M):
			if c_lab[i][j] == '0':
				safe += 1
	return safe

def wall(count, lab, st):
	if count == 3:
		c_lab = copy.deepcopy(lab)
		temp = bfs(c_lab)
		global result
		if temp > result:
			result = temp 
		return
	for t in range((st[0] * M) + st[1], N * M):
		if lab[t // M][t % M] == '0':
			lab[t // M][t % M] = '1'
			wall(count + 1, lab, [t // M, t % M])
			lab[t // M][t % M] = '0'
	return

N, M = map(int, sys.stdin.readline().split())
lab = []
virus = []
for i in range(N):
	lab.append(list(sys.stdin.readline().split()))
	for j in range(M):
		if lab[i][j] == '2':
			virus.append([i, j])
wall(0, lab, [0, 0])
print(result)