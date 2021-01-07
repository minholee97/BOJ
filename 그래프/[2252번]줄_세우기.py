# https://www.acmicpc.net/problem/2252

from collections import deque

N, M = map(int, input().split())
result = ""
e1 = [[] for i in range(N)]
e2 = [0 for i in range(N)]
q = deque()

for i in range(M):
	A, B = map(int, input().split())
	e1[A - 1].append(B - 1)
	e2[B - 1] += 1

for i in range(N):
	if e2[i] == 0:
		q.append(i)

while True:
	if len(q) == 0:
		break
	index = q.popleft()
	result += str(index + 1) + " "
	while True:
		if len(e1[index]) == 0:
			break
		i = e1[index].pop()
		e2[i] -= 1
		if e2[i] == 0:
			q.append(i)

print(result)