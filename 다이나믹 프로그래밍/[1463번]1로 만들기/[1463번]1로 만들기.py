import sys

N = int(sys.stdin.readline().rstrip())

DP = [0] * 1000001
DP[1], DP[2], DP[3] = 0, 1, 1
if N >= 4:
	for i in range(4, N+1):
		p = []
		if i % 3 == 0:
			p.append(DP[i // 3] + 1)
		if i % 2 == 0:
			p.append(DP[i // 2] + 1)
		p.append(DP[i - 1] + 1)
		DP[i] = min(p)
print(DP[N])