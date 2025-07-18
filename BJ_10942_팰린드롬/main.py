# import
import sys

# main
N = int(sys.stdin.readline().rstrip('\n'))
nums = list(map(int, sys.stdin.readline().rstrip('\n').split()))

# i(S 지점), j(E 지점)까지의 팰린드롬 여부 저장
dp = [[1 if _ == __ else 0 for __ in range(N)] for _ in range(N)]
for dt in range(1, N):
    for i in range(N - dt):
        j = i + dt
        # 시작 지점과 끝 지점의 숫자가 같으면서
        # 숫자가 2개인 경우,
        # 양 쪽 끝에 숫자가 추가되기 전에 이미 팰린드롬이었던 경우,
        if nums[i] == nums[j] and (i == j - 1 or dp[i + 1][j - 1] == 1):
            dp[i][j] = 1

M = int(sys.stdin.readline().rstrip('\n'))
for m in range(M):
    S, E = map(int, sys.stdin.readline().rstrip('\n').split())
    print(dp[S - 1][E - 1])
