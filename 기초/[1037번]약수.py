# https://www.acmicpc.net/problem/1037

import sys

l = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
if l == 1:
	print(A[0] * A[0])
else:
	print(A[0] * A[len(A) - 1])