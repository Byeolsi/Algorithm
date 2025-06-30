# 2284 ms

# import
import sys


# main
N, M = map(int, sys.stdin.readline().rstrip('\n').split())
A = list(map(int, sys.stdin.readline().rstrip('\n').split()))
B = list(map(int, sys.stdin.readline().rstrip('\n').split()))

i, j = 0, 0
while i < N and j < M:
    if A[i] < B[j]:
        print(A[i], end=' ')
        i += 1
    else:
        print(B[j], end=' ')
        j += 1

while i < N:
    print(A[i], end=' ')
    i += 1

while j < M:
    print(B[j], end=' ')
    j += 1
