# https://www.acmicpc.net/problem/1948

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
result = []
path = [[] for _ in range(N)]
r_path = [[] for _ in range(N)]
visited = [0 for _ in range(N)]
r_visited = [0 for _ in range(N)]
ind = [0 for _ in range(N)]
for _ in range(M):
	st, ds, t = map(int, sys.stdin.readline().split())
	path[st - 1].append([ds - 1, t])
	r_path[ds - 1].append([st - 1, t])
	ind[ds - 1] += 1
start, dest = map(int, sys.stdin.readline().split())
q = deque()
q.append(start - 1)
while len(q) != 0:
	c = q.popleft()
	for i in range(len(path[c])):
		r, t = path[c][i][0], path[c][i][1]
		ind[r] -= 1
		if visited[r] < t + visited[c]:
			visited[r] = t + visited[c]
		if ind[r] == 0:
			q.append(r)
q = deque()
q.append(dest - 1)
while len(q) != 0:
	c = q.popleft()
	for i in range(len(r_path[c])):
		r, t = r_path[c][i][0], r_path[c][i][1]
		if visited[c] - t == visited[r]:
			if not [c, r] in result:
				result.append([c, r])
			if r_visited[r] == 0:
				r_visited[r] = 1
				q.append(r)
print(str(visited[dest - 1]) + '\n' + str(len(result)))