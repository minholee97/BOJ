# https://www.acmicpc.net/problem/1005

import sys
from collections import deque
result = []
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
	N, K = map(int, sys.stdin.readline().split())
	D = list(map(int, sys.stdin.readline().split()))
	order = [[] for _ in range(N)]
	ind = [0 for _ in range(N)]
	visited = [0 for _ in range(N)]
	for _ in range(K):
		st, ds = map(int, sys.stdin.readline().split())
		order[st - 1].append(ds - 1)
		ind[ds - 1] += 1
	W = int(sys.stdin.readline().rstrip())
	q = deque()
	for i in range(N):
		if ind[i] == 0:
			q.append(i)
			visited[i] = D[i]
	while len(q) != 0:
		c = q.pop()
		for i in range(len(order[c])):
			n = order[c][i]
			if visited[n] != 0:
				visited[n] = max(visited[n], visited[c] + D[n])
				ind[n] -= 1
			else:
				visited[n] = visited[c] + D[n]
				ind[n] -= 1
			if ind[n] == 0:
				q.append(n)
		if ind[W - 1] == 0:
			result.append(visited[W - 1])
			break
for i in range(len(result)):
	print(result[i])