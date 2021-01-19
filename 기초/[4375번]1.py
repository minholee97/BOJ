# https://www.acmicpc.net/problem/4375

import sys

while True:
	try:
		n = int(sys.stdin.readline().rstrip())
	except:
		break
	one = 1
	while True:
		if one % n == 0:
			print(len(str(one)))
			break
		else:
			one = one * 10 + 1