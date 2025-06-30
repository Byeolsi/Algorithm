# 44 ms

# import
import sys


# function
def find(a):
    # 부모 노드가 삭제된 노드이면
    if p[a] == -2:
        return -2
    # 루트 노드이면
    elif p[a] == -1:
        return a

    result = find(p[a])
    # 반환된 값이 -2이면 현재 노드 a도 삭제(부모 노드 번호: -2)
    if result == -2:
        p[a] = result

    # 모든 자식 노드는 result에 따라 삭제되거나 보류
    return result


# main
sys.setrecursionlimit(10**6)

answer = 0

N = int(sys.stdin.readline().rstrip('\n'))
p = list(map(int, sys.stdin.readline().rstrip('\n').split()))
D = int(sys.stdin.readline().rstrip('\n'))
is_leaf = [True for _ in range(N)]

# D번 노드 삭제(부모 노드 번호: -2)
p[D] = -2

# 모든 노드부터 시작해서 부모 노드가 삭제된 노드인지 확인
for i in range(N):
    find(i)

for i in range(N):
    # 자신을 가리키는 노드가 있는 경우(부모 노드인 경우)
    if p[i] >= 0:
        is_leaf[p[i]] = False
    # 삭제된 노드인 경우
    elif p[i] == -2:
        is_leaf[i] = False

# 리프 노드만 True이므로
for i in range(N):
    if is_leaf[i]:
        answer += 1

print(answer)
