import sys
from itertools import combinations_with_replacement

N = int(sys.stdin.readline().rstrip())

data = ['1', '5', '10', '50']

r = list(combinations_with_replacement(data, N))

result = set()

for i in r:
	v = 0
	for j in i:
		v += int(j)
	result.add(v)

print(len(result))