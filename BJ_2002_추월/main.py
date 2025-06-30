# 68 ms

# import
import sys


# main
N = int(sys.stdin.readline().rstrip('\n'))
enter_list = [sys.stdin.readline().rstrip('\n') for _ in range(N)]
exit_list = [sys.stdin.readline().rstrip('\n') for _ in range(N)]

# i: enter_list 포인터
# j: exit_list 포인터
# start: j의 시작 위치
answer = 0
start = 0
i = 0
# start가 N보다 작을 때까지 반복
while start < N:
    # cnt: 추월 개수
    cnt = 0
    # j: start ~ N
    for j in range(start, N):
        # 두 값이 같으면, i와 start를 한 칸 이동, cnt(추월 개수)를 answer에 합산
        if enter_list[i] == exit_list[j]:
            i += 1
            start = j + 1
            answer += cnt
            break
        # 두 값이 다르면, cnt(추월 개수) +1
        else:
            cnt += 1
    # j가 N - 1(exit_list 모두 탐색)이라면, i를 한 칸 이동
    if j >= N - 1:
        i += 1
        
print(answer)
