N = int(input())
result = 0
while True:
	if N % 5 == 0:
		result += N // 5
		break
	else:
		result += 1
		N -= 3
		if N < 0:
			result = -1
			break
print(result)
