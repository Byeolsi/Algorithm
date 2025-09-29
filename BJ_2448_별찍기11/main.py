# 1504 ms

# import #
import sys
from collections import deque


# main #
if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip('\n'))
    q = deque()

    q.append(N - 1)
    while q:
        # 3 줄씩 출력(삼각형 출력)
        line = [[' ' for __ in range(2 * N)] for _ in range(3)]
        is_next_line = [False for _ in range(2 * N)]
        while q:
            cur = q.pop()

            # 삼각형 저장
            line[0][cur] = '*'
            line[1][cur - 1] = '*'
            line[1][cur + 1] = '*'
            for i in range(cur - 2, cur + 3):
                line[2][i] = '*'

            # 다음에 그릴 삼각형(윗 꼭짓점 기준)
            # 중요: 겹치는 경우, 그리지 않음!
            left, right = cur - 3, cur + 3
            if left >= 0:
                is_next_line[left] = not is_next_line[left]
            if right < 2 * N - 1:
                is_next_line[right] = not is_next_line[right]

        # 삼각형 그리기
        for i in range(3):
            print(''.join(line[i]))

        # 다음에 그릴 삼각형의 윗 꼭짓점 큐에 저장
        for i in range(2 * N):
            if is_next_line[i]:
                q.append(i)
