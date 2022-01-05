import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
t = [1]
if N != 1:
    for i in range(2, N + 1):
        t.append(i)
for i in permutations(t, M):
    print(*i)