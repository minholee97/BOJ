# https://www.acmicpc.net/problem/1316

N = int(input())
result = 0
for i in range(N):
	flag = 1
	word = input()
	for j in range(len(word)):
		if word.find(word[j], j + 1) != -1:
			if word.find(word[j], j + 1) != j + 1:
				flag = 0
				break
	result += flag
print(result)