import sys
from collections import deque

def dfs():
	if len(q) == 0:
		return
	c = q.popleft()
	result.append(c)
	for i in range(len(edge[c])):
		t = edge[c][i]
		if visited[t] == False:
			visited[t] = True
			q.append(t)
			dfs()

def bfs():
	while True:
		if len(q) == 0:
			return
		c = q.popleft()
		result.append(c)
		for i in range(len(edge[c])):
			t = edge[c][i]
			if visited[t] == False:
				visited[t] = True
				q.append(t)

N, M, V = map(int, sys.stdin.readline().split())

edge = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
	st, ds = map(int, sys.stdin.readline().split())
	edge[st].append(ds)
	edge[ds].append(st)

for i in range(1, N + 1):
	edge[i].sort()

result = []
q = deque()
q.append(V)
visited[V] = True
dfs()
print(*result)

result = []
q = deque()
q.append(V)
visited = [False for _ in range(N + 1)]
visited[V] = True
bfs()
print(*result)