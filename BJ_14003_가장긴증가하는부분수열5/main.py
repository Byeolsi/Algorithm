# 1256 ms

# import #
import sys
import bisect


# class #
class Solution:
    def solve(self, A: list[int], N: int) -> list[int]:
        tails = []
        length = [0] * N

        # 이진 탐색(Binary Search)
        for i, x in enumerate(A):
            # 배열의 왼쪽부터 시작해서 x가 들어가야 할 위치를 반환
            pos = bisect.bisect_left(tails, x)
            
            # 위치가 마지막이라면 바로 추가
            if pos == len(tails):
                tails.append(x)
            # 아니라면, x로 갱신
            else:
                tails[pos] = x
                
            # 갱신 후, length 업데이트(역추적을 위해)
            length[i] = pos + 1

        result = []
        cur = len(tails)

        # 역추적(Index Tracking)
        for i in range(N - 1, -1, -1):
            # 올바른 순서대로 찾아나감
            if length[i] == cur:
                result.append(A[i])
                cur -= 1
                if cur == 0:
                    break

        return list(reversed(result))


# main #
if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip('\n'))
    A = list(map(int, sys.stdin.readline().rstrip('\n').split()))

    answer = Solution().solve(A, N)
    print(len(answer))
    for x in answer:
        print(x, end=' ')
