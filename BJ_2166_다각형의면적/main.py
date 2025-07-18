# 44 ms

# import
import sys

# main
N = int(sys.stdin.readline().rstrip('\n'))

# 다각형의 면적 공식 적용
answer = 0

init_x, init_y = map(int, sys.stdin.readline().rstrip('\n').split())
prev_x, prev_y = init_x, init_y
for _ in range(1, N):
    x, y = map(int, sys.stdin.readline().rstrip('\n').split())
    
    answer += (prev_x + x) * (prev_y - y)
    prev_x, prev_y = x, y
    
answer += (prev_x + init_x) * (prev_y - init_y)
answer = round(abs(answer) / 2, 1)

print(answer)
