# 112 ms

# import
import sys

# main
N = int(sys.stdin.readline().rstrip('\n'))
solution_list = list(map(int, sys.stdin.readline().rstrip('\n').split()))
solution_list.sort()

min_diff = 2000000000
left, right = 0, N - 1
answer = (solution_list[left], solution_list[right])
while left < right:
    result = solution_list[left] + solution_list[right]
    if min_diff > abs(result):
        min_diff = abs(result)
        answer = (solution_list[left], solution_list[right])
        
    if result < 0:
        left += 1
    else:
        right -= 1

print(answer[0], answer[1])
