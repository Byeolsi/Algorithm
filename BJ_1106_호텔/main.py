# 40 ms

# import
import sys

# global
INF = 1000 * 100
MAX_VALUE = 100

# main
## input
C, N = map(int, sys.stdin.readline().rstrip('\n').split())

promotion_list = []
for _ in range(N):
    cost, people = map(int, sys.stdin.readline().rstrip('\n').split())
    promotion_list.append((cost, people))

## 배낭 알고리즘
dp = [INF for _ in range(C + MAX_VALUE)]
dp[0] = 0
for i in range(C):
    if dp[i] == INF:
        continue

    for cost, people in promotion_list:
        dp[i + people] = min(dp[i + people], dp[i] + cost)

print(min(dp[C:]))
