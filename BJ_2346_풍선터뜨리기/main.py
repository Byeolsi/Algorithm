# 64 ms

# import
import sys
from collections import deque


# main
N = int(sys.stdin.readline().rstrip('\n'))
dq = deque(enumerate(map(int, sys.stdin.readline().rstrip('\n').split())))
answer = []

while dq:
    i, paper = dq.popleft()
    answer.append(i + 1)

    # rotate(1)은 시계 방향으로 1칸 회전(왼쪽으로 이동)
    # rotate(-1)은 반시계 방향으로 1칸 회전(오른쪽으로 이동)
    # popleft()에 의해, 반시계 방향으로 1칸 회전했으므로, paper - 1만큼 회전
    if paper > 0:
        dq.rotate(-(paper - 1))
    # paper가 음수이기 때문에 시계 방향으로 회전하기 위해서는 -paper 만큼 회전
    elif paper < 0:
        dq.rotate(-paper)

print(' '.join(map(str, answer)))
