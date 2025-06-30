# 156 ms

# import
import sys


# main
N = int(sys.stdin.readline().rstrip('\n'))
A = [0] + list(map(int, sys.stdin.readline().rstrip('\n').split()))
dp = [0 for _ in range(N + 1)]

# i번째 값을 기준
for i in range(1, N + 1):
    # 이전에 보았던 값들을 하나씩 확인
    for j in range(i - 1, -1, -1):
        # 현재 기준 값보다 더 작은 값이면서
        # 가장 큰 dp 값을 가지고 있는 값을 탐색
        # 가장 큰 dp 값 + 1
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
