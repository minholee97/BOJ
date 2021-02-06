import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
btns = []
if M != 0:
	btns = list(map(str, sys.stdin.readline().split()))

c1 = abs(N - 100)
c2 = N
c3 = N
cases = []
cases.append(c1)

if M != 10:
	while True:
		f = 0
		c2 = str(c2)
		for i in range(len(c2)):
			if c2[i] in btns:
				f = 1
		c2 = int(c2)
		if f == 0:
			break
		c2 += 1
		if c2 == 1000001:
			c2 = -1
			break

if M != 10:
	while True:
		f = 0
		c3 = str(c3)
		for i in range(len(c3)):
			if c3[i] in btns:
				f = 1
		c3 = int(c3)
		if f == 0:
			break
		c3 -= 1
		if c3 == -1:
			c3 = -1
			break

if c2 != -1 and M != 10:
	cases.append(c2 - N + len(str(c2)))

if c3 != -1 and M != 10:
	cases.append(N - c3 + len(str(c3)))

print(min(cases))
