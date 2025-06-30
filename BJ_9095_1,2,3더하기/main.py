# 40 ms

# import
import sys


# main
T = int(sys.stdin.readline().rstrip('\n'))

for t in range(T):
    n = int(sys.stdin.readline().rstrip('\n'))
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1

    for i in range(1, n + 1):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        if i - 3 >= 0:
            dp[i] += dp[i - 3]

    print(dp[n])
