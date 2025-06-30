# 92 ms

import sys
import collections

# global area
N, M = map(int, sys.stdin.readline().rstrip('\n').split())
nums = list(map(int, sys.stdin.readline().rstrip('\n').split()))

# cnt_nums: 각 숫자의 개수(숫자 기준 오름차순 정렬)
cnt_nums = collections.defaultdict(int)
for num in nums:
    cnt_nums[num] += 1

cnt_nums = sorted([[key, value] for key, value in cnt_nums.items()], key=lambda x: (x[0], x[1]))
N = len(cnt_nums)

# functions
def print_answer(result: list[int]):
    print(' '.join(list(map(str, result))))


def perm(m: int, result: list[int]):
    global M

    if m >= M:
        print_answer(result)
        return

    for i in range(N):
        if cnt_nums[i][1] == 0:
            continue

        cnt_nums[i][1] -= 1
        result.append(cnt_nums[i][0])
        perm(m + 1, result)
        result.pop()
        cnt_nums[i][1] += 1


# main area
perm(0, [])
