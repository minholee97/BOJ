# https://www.acmicpc.net/problem/15652

import sys

def dfs(arr, cnt):
	if cnt == M + 1:
		print(*arr[1:])
		return
	else:
		for i in range(1, N + 1):
			if arr[cnt - 1] > i:
				continue
			arr[cnt] = i
			dfs(arr, cnt+1)

N, M = map(int, sys.stdin.readline().split())

l = [0] * (M + 1)

dfs(l, 1)