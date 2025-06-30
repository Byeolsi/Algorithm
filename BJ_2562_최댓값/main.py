# 40 ms

# import
import sys


# main
max_num = -1
max_index = -1
for i in range(1, 10):
    num = int(sys.stdin.readline().rstrip('\n'))
    if max_num < num:
        max_num = num
        max_index = i

print(max_num)
print(max_index)
