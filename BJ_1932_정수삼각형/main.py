# import
import sys


# main
n = int(sys.stdin.readline().rstrip('\n'))

tri = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(n)]

for i in range(n - 1, 0, -1):
    for j in range(i):
        tri[i - 1][j] += max(tri[i][j], tri[i][j + 1])

print(tri[0][0])
