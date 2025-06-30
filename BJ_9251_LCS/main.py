# 532 ms

# import
import sys


# main
left = [''] + list(sys.stdin.readline().rstrip('\n'))
right = [''] + list(sys.stdin.readline().rstrip('\n'))
dp = [[0 for __ in range(len(right))] for _ in range(len(left))]
answer = ""

# dp[i][j]: left의 0 ~ i번째까지의 문자열와 right의 0 ~ j번째까지의 문자열의 부분 수열의 길
for i in range(1, len(left)):
    for j in range(1, len(right)):
        # left의 i번째 값과 right의 j번째의 값이 같다면,
        # 부분 수열의 길이 + 1
        if left[i] == right[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        # 다르다면,
        # 두 개의 부분 수열의 길이 중 더 긴 것을 선택
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# 부분 수열의 최대 길이 출력
print(dp[-1][-1])
