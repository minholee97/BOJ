import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

d = list(map(int, sys.stdin.readline().split()))
d.sort()

l = map(" ".join, permutations(map(str, d), M))

print("\n".join(l))