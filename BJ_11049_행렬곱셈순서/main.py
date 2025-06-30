# 432 ms - pypy3

# import
import sys


# main
N = int(sys.stdin.readline().rstrip('\n'))
R, C = [], []
dp = [[0 for __ in range(N)] for _ in range(N)]

for i in range(N):
    r, c = map(int, sys.stdin.readline().rstrip('\n').split())
    R.append(r)
    C.append(c)

# 인접한 행렬을 모두 계산하여 dp에 저장
for i in range(N - 1):
    dp[i][i + 1] = R[i] * C[i] * C[i + 1]

# 1. A(BC)의 행렬 모양과 (AB)C의 행렬 모양은 같다.
# 2. 계산 후 행렬의 모양은 반드시 `A_r * C_c`가 된다.
# 3. ABC의 행렬과 DE행렬을 곱하면 계산 결과는 `A_r * C_c * E_c`가 된다.

# K를 어느 특정 중간 지점이라고 정의할 때,
# 결론. {A ~ K} * {(K + 1) ~ E}의 최소 비용 + {A ~ K}의 최소 비용 + {(K + 1) ~ E}의 최소 비용
for j in range(2, N):
    for i in range(N - j):
        dp[i][i + j] = min([R[i] * C[k] * C[i + j] + dp[i][k] + dp[k + 1][i + j] for k in range(i, i + j)])

print(dp[0][N - 1])
