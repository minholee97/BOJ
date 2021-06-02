import sys

N = int(sys.stdin.readline().rstrip())
M = list(map(int, sys.stdin.readline().split()))

d = [[M[i], 0] for i in range(N)]

for i in range(N):
    cur = M[i]
    while True:
        if cur % 3 == 0:
            cur //= 3
            d[i][1] += 1
        else:
            break

d.sort(key=lambda x : (-x[1], x[0]))
for i in range(N):
    print(d[i][0], end=' ')