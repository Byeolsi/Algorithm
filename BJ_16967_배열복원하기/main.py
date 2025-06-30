# 152 ms

# import
import sys


# main
H, W, Y, X = map(int, sys.stdin.readline().rstrip('\n').split())
B = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(H)]

A = [[0 for __ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        A[i][j] = B[i][j]
        # 겹쳐져서 더해진 만큼 다시 뺌
        if i - Y >= 0 and j - X >= 0:
            A[i][j] -= A[i - Y][j - X]

for i in range(H):
    for j in range(W):
        print(A[i][j], end=' ')
    print()
