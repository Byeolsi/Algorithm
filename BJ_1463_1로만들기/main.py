# 704 ms

# import
import sys


# main
X = int(sys.stdin.readline().rstrip('\n'))
dp = [1000000 for _ in range(X + 1)]
dp[X] = 0

for i in range(X, 1, -1):
    if i % 3 == 0:
        dp[i // 3] = dp[i // 3] if dp[i // 3] < dp[i] + 1 else dp[i] + 1
    if i % 2 == 0:
        dp[i // 2] = dp[i // 2] if dp[i // 2] < dp[i] + 1 else dp[i] + 1
        
    dp[i - 1] = dp[i - 1] if dp[i - 1] < dp[i] + 1 else dp[i] + 1

print(dp[1])
