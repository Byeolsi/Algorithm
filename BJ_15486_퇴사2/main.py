# 2720 ms

# import
import sys


# main
N = int(sys.stdin.readline().rstrip('\n'))
T = [0]
P = [0]
dp = [0 for _ in range(N + 1)]
for i in range(N):
    t, p = map(int, sys.stdin.readline().rstrip('\n').split())
    T.append(t)
    P.append(p)

for i in range(1, N + 1):
    # 오늘의 최대값과 이전 날까지의 최대 값 중 큰 값으로 갱신
    dp[i] = max(dp[i], dp[i - 1])

    # 마감일
    post = i + T[i] - 1
    # 마감일이 N번째 날 이내인지 확인
    if post <= N:
        # 마감일의 최대값과 이 작업을 마쳤다는 가정 하에 최대값 중 큰 값으로 갱
        dp[post] = max(dp[post], dp[i - 1] + P[i])

print(dp[N])
