import sys

def dfs(arr, cnt):
	if cnt == M:
		print(*arr)
		return
	else:
		for i in range(1, N + 1):
			arr[cnt] = i
			dfs(arr, cnt + 1)


N, M = map(int, sys.stdin.readline().split())

d = [0] * M

dfs(d, 0)
