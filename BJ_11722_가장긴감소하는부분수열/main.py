# 152 ms

# import
import sys


# main
N = int(sys.stdin.readline().rstrip('\n'))
A = list(map(int, sys.stdin.readline().rstrip('\n').split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        # 현재 기준 값보다 큰 값이 뒤에 있으면
        if A[i] > A[j]:
            # dp 값을 기존 값보다 크면 갱신
            dp[j] = max(dp[j], dp[i] + 1)

# 최대값 찾기
answer = 0
for i in range(N):
    if answer < dp[i]:
        answer = dp[i]

print(answer)
