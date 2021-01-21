# https://www.acmicpc.net/problem/17425

import sys

T = int(sys.stdin.readline().rstrip())

result = [0 for _ in range(1000001)]

for i in range(1, 1000001):
	for j in range(i, 1000001, i):
		result[j] += i
	result[i] += result[i - 1]
for i in range(T):
	N = int(sys.stdin.readline().rstrip())
	print(result[N])