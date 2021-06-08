import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
ind = [0 for _ in range(N + 1)]
sub = [[] for _ in range(N + 1)]
time = [0 for _ in range(N + 1)]
T = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
	M = list(map(int, sys.stdin.readline().split()))
	if M[1] != 0:
		for j in range(len(M[2:])):
			c = M[2:][j]
			sub[c].append(i)
			ind[i] += 1
	time[i] = M[0]
	T[i] = M[0]

q = deque()

for i in range(1, N + 1):
	if ind[i] == 0:
		q.append(i)

while q:
	cur = q.popleft()
	for i in sub[cur]:
		T[i] = max(time[i] + T[cur], T[i])
		ind[i] -= 1
		if ind[i] == 0:
			q.append(i)

print(max(T))