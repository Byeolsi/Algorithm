# 44 ms

# import
import sys


# main
n = int(sys.stdin.readline().rstrip('\n'))


# 타일을 놓는 것을 두 가지로 생각한다.
# 1. 1 * 2 세로 타일을 하나 앞에 놓는다.
    # dp[i] += dp[i - 1]

# 2. 2 * 1 가로 타일 두 개를 앞에 놓는다.
    # 앞의 2 * 1 가로 타일 두 개를 놓기 위해서는 2 * 2 공간이 필요하다.
    # dp[i] += dp[i - 2]

# 결론.
    # dp[i] = dp[i - 1] + dp[i - 2]
    
A, B = 1, 1
for i in range(2, n + 1):
    A, B = B, ((A + B) % 10007)

print(B)
