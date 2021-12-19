import sys

N = int(sys.stdin.readline().rstrip())

dp = [-1 for _ in range(5001)]

dp[3] = 1
dp[5] = 1

if N < 6:
    print(dp[N])
else:
    for i in range(6, N + 1):
        if dp[i - 5] != -1:
            dp[i] = dp[i - 5] + 1
        elif dp[i - 3] != -1:
            dp[i] = dp[i - 3] + 1
        else:
            dp[i] = -1
    print(dp[N])
