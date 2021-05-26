import sys

input_line = list(sys.stdin.readline().rstrip())
prev = None
count = 0
result = 1
for i in input_line:
	value = 0
	if i == prev:
		count = 1
	else:
		count = 0
	if i == 'd':
		value = 10 - count
	else:
		value = 26 - count
	result *= value
	prev = i
print(result)