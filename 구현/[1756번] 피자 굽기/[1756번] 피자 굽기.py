import sys
D, N = map(int, sys.stdin.readline().split())
oven = list(map(int, sys.stdin.readline().split()))
dough= list(map(int, sys.stdin.readline().split()))

prev = oven[0]
for i in range(1, D):
    if oven[i] > prev:
        oven[i] = prev
    prev = oven[i]

pos = 0
left, right = 0, D - 1
for i in dough:
    flag = True
    while left <= right:
        mid = (left + right) // 2
        if oven[mid] >= i:
            left = mid + 1
            pos = mid
            flag = False
        else:
            right = mid - 1
    if flag:
        pos = -1
        break
    left = 0
    right = pos - 1
if pos == -1:
    print(0)
else:
    print(pos + 1)