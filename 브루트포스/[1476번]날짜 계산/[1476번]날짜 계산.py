# https://www.acmicpc.net/problem/1476

import sys

E, S, M = map(int, sys.stdin.readline().split())
e, s, m = 1, 1, 1
year = 1
while True:
	if e == E and s == S and m == M:
		break
	year += 1
	e += 1
	if e == 16:
		e = 1
	s += 1
	if s == 29:
		s = 1
	m += 1
	if m == 20:
		m = 1
print(year)
