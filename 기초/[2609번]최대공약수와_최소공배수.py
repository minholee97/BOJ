# https://www.acmicpc.net/problem/2609

import sys

N = list(map(int, sys.stdin.readline().split()))
N.sort()
a, b = N[0], N[1]
while a != 0:
	r = b % a
	b = a
	a = r
print(str(b) + "\n" + str(N[0] * N[1] // b))