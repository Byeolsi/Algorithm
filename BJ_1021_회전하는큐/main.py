# 44 ms

# import
import sys


# main
N, M = map(int, sys.stdin.readline().rstrip('\n').split())
del_list = list(map(int, sys.stdin.readline().rstrip('\n').split()))

answer = 0
cur = 1
for i in range(M):
    # 현재 위치에서 제거 위치로 이동하기 위한 최단 거리를 계산
    if cur < del_list[i]:
        answer += min(del_list[i] - cur, cur + N - del_list[i])
    else:
        answer += min(cur - del_list[i], del_list[i] + N - cur)
    # 제거 위치가 새로운 현재 위치
    cur = del_list[i]
    # 숫자 개수 감소
    N -= 1
    # 현재 위치보다 더 큰 값을 1씩 감소(앞으로 한 칸씩 당김)
    for j in range(i + 1, M):
        if cur < del_list[j]:
            del_list[j] -= 1
    
print(answer)
