import sys
from itertools import product

T = int(sys.stdin.readline().rstrip())
mark = ['+', '-', ' ']
for _ in range(T):
    result = []
    N = int(sys.stdin.readline().rstrip())
    marks = list(product(mark, repeat=N-1))
    order = [i for i in range(1, N+1)]
    lines = []
    for i in marks:
        temp = ""
        for j in range(len(order)):
            temp += str(order[j])
            if j != len(order) - 1:
                temp += i[j]
        lines.append(temp)
    for i in lines:
        if eval(i.replace(' ', '')) == 0:
            result.append(i)
    result.sort()
    for i in result:
        print(i)
    print()