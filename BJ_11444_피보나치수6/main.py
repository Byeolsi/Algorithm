# 36 ms

# import
import sys

# global
memo = {
    0: 0,
    1: 1
}
remainder = 1000000007


# functions
def fibo(n: int) -> int:
    if n in memo:
        return memo[n]

    # 짝수라면
    if n % 2 == 0:
        memo[n] = (2 * fibo(n // 2 - 1) + fibo(n // 2)) * fibo(n // 2) % remainder
    # 홀수라면
    else:
        memo[n] = (fibo(n // 2 + 1) ** 2 + fibo(n // 2) ** 2) % remainder
    
    return memo[n]


# main
n = int(sys.stdin.readline().rstrip('\n'))

print(fibo(n))
