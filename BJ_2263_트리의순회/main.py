# 228 ms

# import
import sys


# function
def divide_and_conquer(l_in, r_in, l_post, r_post):
    root = postorder[r_post - 1]
    index = inorder_index[root]

    print(root, end=' ')

    # 왼쪽 서브 트리
    if l_in < index:
        divide_and_conquer(l_in, index, l_post, l_post + (index - l_in))
    # 오른쪽 서브 트리
    if r_in > index + 1:
        divide_and_conquer(index + 1, r_in, r_post - (r_in - index), r_post - 1)


# main
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip('\n'))
inorder = list(map(int, sys.stdin.readline().rstrip('\n').split()))
postorder = list(map(int, sys.stdin.readline().rstrip('\n').split()))
# 시간을 줄이기 위해 중위 순회의 인덱스 저장
inorder_index = [0 for _ in range(n + 1)]
for i in range(n):
    inorder_index[inorder[i]] = i

divide_and_conquer(0, n, 0, n)
