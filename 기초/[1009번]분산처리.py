# https://www.acmicpc.net/problem/1009

import sys

T = int(sys.stdin.readline().rstrip())
result = []
for _ in range(T):
	a, b = map(int, sys.stdin.readline().split())
	if a % 10 == 0:
		result.append(10)
		continue
	c = a % 10
	d = 1
	for i in range(b):
		d *= c
		d %= 10
	result.append(d)
for i in range(T):
	print(result[i])