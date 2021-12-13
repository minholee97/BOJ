import sys
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
n = int(sys.stdin.readline().rstrip())
print(solution(n) % 10007)