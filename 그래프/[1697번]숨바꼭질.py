# https://www.acmicpc.net/problem/1697

import sys
import copy
from collections import deque 

N, K = map(int, sys.stdin.readline().split())

q = deque()
q.append([N, 0])
v = [0 for i in range(100001)]
v[N] = 1

while len(q) != 0:
	cur = q.popleft()
	if cur[0] == K:
		print(cur[1])
		break
	if 0 <= cur[0] + 1 <= 100000:
		if v[cur[0] + 1] == 0:
			q.append([cur[0] + 1, cur[1] + 1])
			v[cur[0] + 1] = 1
	if 0 <= cur[0] - 1 <= 100000:
		if v[cur[0] - 1] == 0:
			q.append([cur[0] - 1, cur[1] + 1])
			v[cur[0] - 1] = 1
	if 0 <= cur[0] * 2 <= 100000:
		if v[cur[0] * 2] == 0:
			q.append([cur[0] * 2, cur[1] + 1])
			v[cur[0] * 2]