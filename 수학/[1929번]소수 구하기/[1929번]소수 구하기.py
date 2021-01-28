# https://www.acmicpc.net/problem/1929

import sys

M, N = map(int, sys.stdin.readline().split())

num = [i for i in range(1000001)]

for i in range(2, 1001):
	for j in range(i * 2, 1000001, i):
		num[j] = 0

num[1] = 0

for i in range(M, N + 1):
	if num[i] != 0:
		print(num[i])