# 3356 ms

# import
import sys


# main
N, K = map(int, sys.stdin.readline().rstrip('\n').split())
W = []
V = []
for i in range(N):
    w, v = map(int, sys.stdin.readline().rstrip('\n').split())
    W.append(w)
    V.append(v)

# dp를 무게를 기준으로 인덱스를 정의
# 해당 무게에서 가질 수 있는 최대값으로 갱신
dp = [0 for i in range(K + 1)]
for w, v in zip(W, V):
    # 맨 끝에서부터 반복해야 갱신 결과가 새로운 결과에 영향을 주지 않음.
    for i in range(K, w - 1, -1):
        # 기존 값과 이전 값에 새로운 물건의 가치를 더한 값과 비교
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[-1])
