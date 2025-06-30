# 1268 ms - pypy3

# import
import sys


# main
T = int(sys.stdin.readline().rstrip('\n'))

for t in range(T):
    N = int(sys.stdin.readline().rstrip('\n'))
    chs = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    dp = [[0 for __ in range(N)] for _ in range(N)]

    # 이어져 있는 파일끼리 연결했을 때의 비용
    for i in range(N - 1):
        dp[i][i + 1] = chs[i] + chs[i + 1]

    # 점점 범위를 키워가면서 가장 작은 비용을 선택
    # dp[0][3] = min([
    #   dp[0][0] + dp[1][3],
    #   dp[0][1] + dp[2][3],
    #   dp[0][2] + dp[3][3]
    # ])
    for j in range(2, N):
        for i in range(N - j):
            dp[i][i + j] = min([dp[i][k] + dp[k + 1][i + j] for k in range(i, i + j)]) + sum(chs[i:i + j + 1])

    print(dp[0][N - 1])
