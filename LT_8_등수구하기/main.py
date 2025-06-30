# import
import sys


# main
N = int(sys.stdin.readline().rstrip('\n'))
nums = list(map(int, sys.stdin.readline().rstrip('\n').split()))
cnt = {}
dp = [0 for _ in range(101)]
dp[100] = 1

for i in range(N):
    if nums[i] not in cnt:
        cnt[nums[i]] = 0
    cnt[nums[i]] += 1

for i in range(99, -1, -1):
    dp[i] += dp[i + 1]
    if i + 1 in cnt:
        dp[i] += cnt[i + 1]

for i in range(N):
    print(dp[nums[i]], end=' ')
