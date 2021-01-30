# https://www.acmicpc.net/problem/2309

import sys
from itertools import combinations

height = []
for _ in range(9):
	height.append(int(sys.stdin.readline().rstrip()))

dwarf = list(combinations(height, 7))
result = []
for i in range(len(dwarf)):
	if sum(dwarf[i]) == 100:
		result = list(dwarf[i])

result.sort()
for i in range(7):
	print(result[i])
