# 36 ms

# import #
import sys


# class #
class Solution:
    def __init__(self, matrix: list[list]):
        self.memo = {}
        self.memo[1] = matrix


    # 행렬 곱셈
    def matrix_multiple(self, A: list[list], B: list[list]) -> list[list]:
        result = [[0 for __ in range(len(A[_]))] for _ in range(len(A))]

        for i in range(len(A)):
            for k in range(len(B)):
                for j in range(len(A[i])):
                    result[i][k] += (A[i][j] * B[j][k]) % 1000
                    result[i][k] %= 1000

        return result


    # 행렬 제곱
    def matrix_expo(self, expo: int) -> list[list]:
        # 메모되어 있는 연산 결과 반환
        if expo in self.memo:
            return self.memo[expo]

        # 이분 탐색
        left = self.matrix_expo(expo // 2)
        right = self.matrix_expo(expo - expo // 2)
        # 연산 결과 메모
        self.memo[expo] = self.matrix_multiple(left, right)

        return self.memo[expo]
        

# main #
if __name__ == "__main__":
    N, B = map(int, sys.stdin.readline().rstrip('\n').split())
    matrix = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
    # 예외: 행렬의 각 원소가 1000인 경우
    # 진짜 문제 더럽고 치사하다...
    for i in range(N):
        for j in range(N):
            matrix[i][j] %= 1000

    answer = Solution(matrix).matrix_expo(B)
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            print(answer[i][j], end=' ')
        print()
