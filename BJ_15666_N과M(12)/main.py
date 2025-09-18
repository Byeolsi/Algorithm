# 44 ms

# import #
import sys


# class #
class Solution:
    def __init__(self, nums: list[int], K: int):
        self.nums = nums
        self.K = K
        self.answer = list()
    

    # 중복 순열
    def perm(self, result: list[int], index: int, n: int):
        if n >= self.K:
            self.answer.append(result)
            return

        for i in range(index, len(self.nums)):
            self.perm(result + [self.nums[i]], i, n + 1)


    def print_answer(self):
        for i in range(len(self.answer)):
            for j in range(len(self.answer[i])):
                print(self.answer[i][j], end=' ')
            print()


# main #
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip('\n').split())
    nums = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    nums = list(set(nums))  # 중복 제거
    nums.sort()             # 오름차순 정렬

    sol = Solution(nums, M)
    sol.perm([], 0, 0)
    sol.print_answer()
