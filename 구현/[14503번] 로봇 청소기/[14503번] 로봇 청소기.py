import sys

def rotate(v):
    if v == 0:
        v = 3
    else:
        v -= 1
    return v

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
count   = 0
room    = []
clean   = [[False for _ in range(M)] for _ in range(N)]
head    = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for _ in range(N):
    room.append(sys.stdin.readline().split())
while True:
    if clean[r][c] == False:
        clean[r][c] = True
        count += 1
    flag = 0
    for i in range(4):
        d = rotate(d)
        dx, dy = r + head[d][0], c + head[d][1]
        
        if room[dx][dy] == '1':
            continue
        if clean[dx][dy] == True:
            continue
        flag = 1
        r, c = dx, dy
        break
    if flag == 0:
        back = rotate(rotate(d))
        dx, dy = r + head[back][0], c + head[back][1]
        if room[dx][dy] == '1':
            break
        r, c = dx, dy
print(count)