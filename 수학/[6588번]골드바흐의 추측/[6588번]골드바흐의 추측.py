# https://www.acmicpc.net/problem/6588

import sys

prime = [i for i in range(1000001)]
prime[1] = 0

for i in range(2, 1001):
	if prime[i] != 0:
		for j in range(i * 2, 1000001, i):
			prime[j] = 0

while True:
	n = int(sys.stdin.readline().rstrip())
	if n == 0:
		break
	for i in range(3, n + 1):
		if prime[i] == 0 or prime[n - i] == 0:
			continue
		print(str(n) + " = " + str(i) + " + " + str(n - i))
		break
		if i == n:
			print("Goldbach's conjecture is wrong.")
