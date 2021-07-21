import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
mp = []
wall = []
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(N):
	line = list(map(int, sys.stdin.readline().split()))
	for j in range(M):
		if line[j] == 1:
			wall.append([i, j])
	mp.append(line)
H, W, Sr, Sc, Fr, Fc = map(int, sys.stdin.readline().split())
visited = [[False for _ in range(M)] for _ in range(N)]

q = deque()
q.append([Sr, Sc, 0])
result = 0
flag = 0
visited[Sr - 1][Sc - 1] = True
while len(q) != 0:
	cur = q.popleft()
	if cur[0] == Fr and cur[1] == Fc:
		result = cur[2]
		flag = 1
		break
	for i in move:
		x = cur[0] + i[0]
		y = cur[1] + i[1]
		false = 0
		if (0 < x and (x + H - 1) <= N) and (0 < y and (y + W - 1) <= M) and (visited[x - 1][y - 1] == False):
			dx = x - 1
			dy = y - 1
			for j in wall:
				if dx <= j[0] and j[0] < dx + H and dy <= j[1] and j[1] < dy + W:
					false = 1
					break
			if false == 0:
				q.append([x, y, cur[2] + 1])
				visited[x - 1][y - 1] = True
if flag == 0:
	print(-1)
else:
	print(result)