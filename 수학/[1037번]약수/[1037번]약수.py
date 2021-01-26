# https://www.acmicpc.net/problem/1037

import sys

l = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
print(A[0] * A[-1])
