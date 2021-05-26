import sys

A, B, C, X, Y = map(int, sys.stdin.readline().split())

total = 0

if A + B > 2 * C:
	if X > Y:
		if A < 2 * C:
			total += 2 * C * Y + A * (X - Y)
		else:
			total += 2 * C * X
	else:
		if B < 2 * C:	
			total += 2 * C * X + B * (Y - X)
		else:
			total += 2 * C * Y
else:
	total += A * X + B * Y

print(total)	