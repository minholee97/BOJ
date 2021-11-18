import sys

H, W = map(int, sys.stdin.readline().split())
B = list(map(int, sys.stdin.readline().split()))

world = [[0 for _ in range(W)] for _ in range(H)]

for i in range(W):
    for j in range(H - 1, (H - 1) - (B[i] - 1) - 1, -1):
        world[j][i] = 1
result = 0
for i in range(H):
    wall = 0
    temp = 0 
    for j in range(W):
        if wall == 0 and world[i][j] == 1:
            wall = 1
        elif wall == 1 and world[i][j] == 0:
            temp += 1
        elif wall == 1 and world[i][j] == 1:
            result += temp
            temp = 0

print(result)