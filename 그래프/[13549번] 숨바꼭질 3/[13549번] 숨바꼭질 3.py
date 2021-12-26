import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [False for _ in range(100001)]
q = deque()
q.append([N, 0])
while True:
    if len(q) == 0:
        break
    cur = q.popleft()
    if cur[0] == K:
        print(cur[1])
        break
    visited[cur[0]] = True
    if cur[0] + 1 < 100001 and visited[cur[0] + 1] == False:
        q.append([cur[0] + 1, cur[1] + 1])
    if cur[0] - 1 > -1 and visited[cur[0] - 1] == False:
        q.append([cur[0] - 1, cur[1] + 1])
    if cur[0] * 2 < 100001 and visited[cur[0] * 2] == False:
        q.appendleft([cur[0] * 2, cur[1]])
