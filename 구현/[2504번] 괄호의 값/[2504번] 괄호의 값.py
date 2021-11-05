import sys
from collections import deque

s = sys.stdin.readline().rstrip()
result = 0
back = 0
b = deque()
v  = deque()
for i in s:
    if i == '(':
        b.append(i)
        v.append(i)
    elif i == '[':
        b.append(i)
        v.append(i)
    elif i == ')':
        if len(v) == 0:
            print(0)
            exit()
        temp = v.pop()
        if len(b) == 0 or b.pop() == '[':
            print(0)
            exit()
        if type(temp) == int:
            temp2 = temp * 2
            if len(v) != 0 and type(v[-1]) == int:
                v.append(v.pop() + temp2)
            else:
                v.pop()
                if len(v) != 0 and type(v[-1]) == int:
                    v.append(v.pop() + temp2)
                else:
                    v.append(temp2)
        else:
            if len(v) != 0 and type(v[-1]) == int:
                v.append(v.pop() + 2)
            else:
                v.append(2)
    else:
        if len(v) == 0:
            print(0)
            exit()
        temp = v.pop()
        if len(b) == 0 or b.pop() == '(':
            print(0)
            exit()
        if type(temp) == int:
            temp2 = temp * 3
            if len(v) != 0 and type(v[-1]) == int:
                v.append(v.pop() + temp2)
            else:
                v.pop()
                if len(v) != 0 and type(v[-1]) == int:
                    v.append(v.pop() + temp2)
                else:
                    v.append(temp2)
        else:
            if len(v) != 0 and type(v[-1]) == int:
                v.append(v.pop() + 3)
            else:
                v.append(3)
if len(v) != 1 or type(v[0]) == str:
    print(0)
else:
    print(v.pop())