# 2480 ms

# import #
import sys


# global #
INF = 3000000001


# main #
N = int(sys.stdin.readline().rstrip('\n'))
nums = list(map(int, sys.stdin.readline().rstrip('\n').split()))
nums.sort()

# functions #
# 슬라이딩 윈도우
def sliding_window(N, nums):
    min_diff = INF
    answer = [0, 0, 0]
    for i in range(N - 2):
        left, right = i + 1, N - 1
        while left < right:
            result = nums[i] + nums[left] + nums[right]
            if min_diff > abs(result):
                 min_diff = abs(result)
                 answer = [nums[i], nums[left], nums[right]]

            if result < 0:
                left += 1
            elif result > 0:
                right -= 1
            else:
                return answer

    return answer


print(' '.join(map(str, sliding_window(N, nums))))
