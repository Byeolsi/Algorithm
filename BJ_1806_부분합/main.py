# 100 ms

# import
import sys

# global
INF = 100000

# main
N, S = map(int, sys.stdin.readline().rstrip('\n').split())
nums = list(map(int, sys.stdin.readline().rstrip('\n').split()))

# 슬라이딩 윈도우 적용
answer = INF
left, right = 0, 1
acc_sum = nums[left]
while right < N:
    if acc_sum >= S:
        answer = min(answer, right - left)
        acc_sum -= nums[left]
        left += 1
    else:
        acc_sum += nums[right]
        right += 1

# 누적합이 S보다 큰 경우, left 값을 감산하는 것을 반복
while acc_sum >= S:
    answer = min(answer, right - left)
    acc_sum -= nums[left]
    left += 1

print(answer % INF)
