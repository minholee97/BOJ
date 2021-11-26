import sys

N, X = map(int, sys.stdin.readline().split())
menu = []
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    if A >= B:
        menu.append([A - B, 'A', A, B])
    else:
        menu.append([B - A, 'B', B, A])

result = 0
menu.sort(key = lambda x : x[0], reverse=True)
for i in range(N):
    if ((N - i - 1) * 1000) > (X - 5000):
        if menu[i][1] == 'A':
            result += menu[i][3]
        else:
            result += menu[i][2]
        X -= 1000
    else:
        if menu[i][1] == 'A':
            result += menu[i][2]
            X -= 5000
        else:
            result += menu[i][2]
            X -= 1000 
print(result)