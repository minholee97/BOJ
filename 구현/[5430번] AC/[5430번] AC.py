import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
results = []
for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    x = (sys.stdin.readline().rstrip())
    if n == 0:
        x = []
    else:
        x = list(x[1:-1].split(','))
    x = deque(x)
    reverse = 1
    for i in range(len(p)):
        order = p[i]
        if order == 'D':
            if len(x) == 0:
                reverse = 1
                x = deque([-1])
                break
            if reverse == 1:
                x.popleft()
            elif reverse == -1:
                x.pop()
        elif order == 'R':
            reverse *= -1
    if reverse == -1:
        x.reverse()
    results.append(x)
for i in results:
    if len(i) == 0:
        print("[]")
        continue
    result = "["
    for j in range(len(i)):
        if i[j] == -1:
            result = "error"
            break
        if j != len(i) - 1:
            result += i[j] + ','
        else:
            result += i[j] + ']'
    print(result)