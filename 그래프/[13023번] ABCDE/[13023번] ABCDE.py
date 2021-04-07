# https://www.acmicpc.net/problem/13023

import sys

def dfs(p, c):
	visited[p] = True
	c += 1
	if c == 5:
		global flag
		flag = 1
		return
	for i in rel[p]:
		if visited[i] == False:
			dfs(i, c)
			if flag == 1:
				return
			visited[i] = False

N, M = map(int, sys.stdin.readline().split())
rel = [[] for _ in range(N)]
visited = [False for _ in range(N)]
flag = 0

for _ in range(M):
	s, d = map(int, sys.stdin.readline().split())
	rel[s].append(d)
	rel[d].append(s)	

for i in range(N):
	dfs(i, 0)
	visited = [False for _ in range(N)]
	if flag == 1:
		print("1\n")
		break
if flag == 0:
	print("0\n")