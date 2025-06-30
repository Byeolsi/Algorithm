# 31216 ms

# import
import sys


# global
answer = 0


# function
def is_overlap(row):
    # 이전에 선택한 모든 퀸의 위치를 모두 확인
    # 이전 배치한 퀸들과 공격 범위가 겹친다면 False 반환
    for i in range(row):
        # 열 위치가 겹치는지, 대각선 위치가 겹치는지
        if set_q[i] == set_q[row] or abs(i - row) == abs(set_q[i] - set_q[row]):
            return True
    return False


def dfs(row):
    global answer
    
    if row >= N:
        answer += 1
        return

    # 순서대로 하나씩 넣어보고, 공격 범위가 겹치는지 확인
    for i in range(N):
        set_q[row] = i
        # 겹치지 않으면, 다음 행으로
        if not is_overlap(row):
            dfs(row + 1)


# main
N = int(sys.stdin.readline().rstrip('\n'))
# 인덱스가 행, 값이 열
set_q = [0 for _ in range(N)]

dfs(0)
print(answer)
