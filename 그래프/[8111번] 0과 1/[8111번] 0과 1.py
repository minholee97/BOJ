import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

while T > 0:
	N = int(sys.stdin.readline().rstrip())
	q = deque()
	visited = [False for _ in range(20001)]
	if N == 1:
		print('1')
	else:
		q.append([1, "1"])
		visited[1] = True
		flag = 0
		while len(q) != 0:
			cur = q.popleft()
			nodes = [(cur[0] * 10) % N, (cur[0] * 10 + 1) % N]
			p = -1
			for node in nodes:
				p += 1
				if visited[node] == True:
					continue
				if node == 0:
					print(cur[1] + str(p))
					flag = 1
					break
				visited[node] = True
				q.append([node, cur[1] + str(p)])
			if flag == 1:
				break
	T -= 1