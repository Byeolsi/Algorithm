# 60 ms

# import #
import sys
from collections import deque


# class #
class Solution:
    def greedy(self, A, B):
        answer = 1  # 처음 시작 숫자도 포함

        while B != A:
            if B < A:
                return -1
            if B % 10 == 1:  # 끝자리가 1이면(즉, 홀수)
                B //= 10
                answer += 1
            elif B % 2 == 0:  # 짝수면
                B //= 2
                answer += 1
            else:  # 어떤 연산으로도 못 줄이는 경우
                return -1

        return answer


# main #
if __name__ == "__main__":
    A, B = map(int, sys.stdin.readline().rstrip('\n').split())
    print(Solution().greedy(A, B))
