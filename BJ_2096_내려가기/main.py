# 656 ms

# import #
import sys


# main #
if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip('\n'))

    max_dp = [[0 for __ in range(3)] for _ in range(2)]
    min_dp = [[9 * 100000 for __ in range(3)] for _ in range(2)]

    numbers = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    max_dp[0] = numbers[:]
    min_dp[0] = numbers[:]
    # 최댓값, 최소값 찾기
    for i in range(N - 1):
        numbers = list(map(int, sys.stdin.readline().rstrip('\n').split()))
        for j in range(3):
            if j - 1 >= 0:
                max_dp[1][j - 1] = max(max_dp[1][j - 1], max_dp[0][j] + numbers[j - 1])
                min_dp[1][j - 1] = min(min_dp[1][j - 1], min_dp[0][j] + numbers[j - 1])
            max_dp[1][j] = max(max_dp[1][j], max_dp[0][j] + numbers[j])
            min_dp[1][j] = min(min_dp[1][j], min_dp[0][j] + numbers[j])
            if j + 1 < 3:
                max_dp[1][j + 1] = max(max_dp[1][j + 1], max_dp[0][j] + numbers[j + 1])
                min_dp[1][j + 1] = min(min_dp[1][j + 1], min_dp[0][j] + numbers[j + 1])

        # dp 값 옮기기
        for j in range(3):
            max_dp[0][j] = max_dp[1][j]
            min_dp[0][j] = min_dp[1][j]
        # dp 값 초기화
        for j in range(3):
            max_dp[1][j] = 0
            min_dp[1][j] = 9 * 100000

    print(max(max_dp[0]), min(min_dp[0]))
