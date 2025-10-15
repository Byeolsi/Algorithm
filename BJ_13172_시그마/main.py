# 280 ms

# import #
import sys


# global #
MOD = 1000000007
memo = {}


# function #
def divide_and_conquer(a: int, b: int):
    if b in memo:
        return memo[b]

    memo[b] = divide_and_conquer(a, b // 2) * divide_and_conquer(a, b - b // 2) % MOD
    return memo[b]


# main #
sys.setrecursionlimit(10 ** 6)

if __name__ == "__main__":
    M = int(sys.stdin.readline().rstrip('\n'))

    answer = 0
    for i in range(M):
        N, S = map(int, sys.stdin.readline().rstrip('\n').split())
        
        memo = {}
        memo[1] = N
        # N^(-1) = N^(MOD - 2) % MOD
        inv_N = divide_and_conquer(N, MOD - 2)

        # E_i = S * N^(-1) % MOD
        answer += S * inv_N % MOD
        # E = E_1 + E_2 + E_3 + ... + E_M
        answer = answer % MOD

    print(answer)
