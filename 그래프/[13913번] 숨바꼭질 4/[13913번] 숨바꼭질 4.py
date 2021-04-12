import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
v = [-1] * 100001
v[N] = -2

if N > K:
	cnt = 0
	path = [N]
	while N != K:
		cnt += 1
		N -= 1
		path.append(N)
	print(cnt)
	print(*path)

else:
	q = deque()
	q.append([0, N])
	while len(q) != 0:
		c = q.popleft()
		cnt = c[0]
		loc = c[1]
		if loc == K:
			print(cnt)
			path = []
			path.append(loc)
			t = loc
			while v[t] != -2:
				path.append(v[t])
				t = v[t]
			print(*path[::-1])
			break
		if loc > 0:
			if v[loc - 1] == -1:
				v[loc - 1] = loc
				q.append([cnt+1, loc-1])
		if loc < 100000:
			if v[loc + 1] == -1:
				v[loc + 1] = loc
				q.append([cnt+1, loc+1])
		if loc < 50001:
			if v[loc * 2] == -1:
				v[loc * 2] = loc
				q.append([cnt+1, loc*2])