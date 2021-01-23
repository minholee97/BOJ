# https://www.acmicpc.net/problem/1978

import sys

N = int(sys.stdin.readline().rstrip())
M = list(map(int, sys.stdin.readline().split()))
num = [0] * 1001
count = 0
for i in range(1, 1001):
	for j in range(i, 1001, i):
		num[j] += 1
for i in range(N):
	if num[M[i]] == 2:
		count += 1
print(count)