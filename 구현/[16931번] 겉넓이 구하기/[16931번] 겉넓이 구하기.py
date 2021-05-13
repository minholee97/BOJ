import sys

N, M = map(int, sys.stdin.readline().split())

shape = []

for i in range(N):
	line = list(map(int, sys.stdin.readline().split()))
	shape.append(line)

result = 0
for i in range(N):
	total = shape[i][0]
	for j in range(M - 1):
		total += abs(shape[i][j] - shape[i][j + 1])
	total += shape[i][-1]
	result += total

for i in range(M):
	total = shape[0][i]
	for j in range(N - 1):
		total += abs(shape[j][i] - shape[j + 1][i])
	total += shape[-1][i]
	result += total

result += (N * M * 2)

print(result)