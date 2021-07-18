import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

q = deque()
q.append([N, 0])
visited = [-1 for _ in range(500001)]
visited2 = [-1 for _ in range(500001)]
visited[N] = 0
 
while len(q) != 0:
	cur = q.popleft()
	moving = [cur[0] - 1, cur[0] + 1, cur[0] * 2]
	t = cur[1] + 1
	for move in moving:
		if move < 0 or move > 500000:
			continue
		if t % 2 == 0:
			if visited[move] > t or visited[move] == -1:
				visited[move] = t
				q.append([move, t])
		else:
			if visited2[move] > t or visited2[move] == -1:
				visited2[move] = t
				q.append([move, t])
time = 0
result = []
while K < 500001:
	if visited[K] == time or visited2[K] == time:
		result.append(time)
	elif (visited[K] % 2 == time % 2 and visited[K] < time) or (visited2[K] % 2 == time % 2 and visited2[K] < time):
		result.append(time)
	time += 1
	K += time
	if K >= 500001 and len(result) == 0:
		result.append(-1)

print(min(result))