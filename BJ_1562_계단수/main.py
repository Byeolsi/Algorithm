# 512 ms

# import #
import sys


# global #
NUM_RANGE = 10 # 0 ~ 9
BIT_RANGE = 1 << NUM_RANGE # 9876543210 (0b0000000000 ~ 0b1111111111)
MOD = 10 ** 9


# functions #
def solution(n: int) -> int:
    # dp[자리 수][마지막 숫자][사용된 숫자들의 비트필드]
    dp = [[[0] * BIT_RANGE for _ in range(NUM_RANGE)] for _ in range(n + 1)]

    # 한자리 수 부터 시작하려면 한자리 수들 다 1로 초기화
    for num in range(NUM_RANGE):
        dp[1][num][1 << num] = 1

    for i in range(1, n): # n - 1까지 하면 n을 구할 수 있음
        for j in range(NUM_RANGE):
            for bit in range(BIT_RANGE):
                if 0 <= j < 9:
                    up = bit | 1 << (j + 1)
                    dp[i + 1][j + 1][up] += dp[i][j][bit]
                    dp[i + 1][j + 1][up] %= MOD
                if 0 < j <= 9:
                    down = bit | 1 << (j - 1)
                    dp[i + 1][j - 1][down] += dp[i][j][bit]
                    dp[i + 1][j - 1][down] %= MOD

    answer = 0
    for num in range(1, NUM_RANGE): # 0으로 시작하는 수만 제외
        answer += dp[n][num][0b1111111111]
        answer %= MOD

    return answer


# main #
if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip('\n'))

    print(solution(n))
