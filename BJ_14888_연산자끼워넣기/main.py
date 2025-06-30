# 76 ms

# import
import sys


# functions
def perm(index, result):
    global max_answer
    global min_answer
    # global symbols
    
    if index >= N:
        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)
        return

    for i in range(4):
        if symbols[i] <= 0:
            continue

        symbols[i] -= 1
        # 0은 '+'
        if i == 0:
            perm(index + 1, result + numbers[index])
        # 1은 '-'
        elif i == 1:
            perm(index + 1, result - numbers[index])
        # 2은 '*'
        elif i == 2:
            perm(index + 1, result * numbers[index])
        # 3은 '//'
        else:
            if result >= 0:
                perm(index + 1, result // numbers[index])
            else:
                perm(index + 1, (-1) * ((-1) * result // numbers[index]))
        symbols[i] += 1


# main
max_answer = (-1) * sys.maxsize - 1
min_answer = sys.maxsize

N = int(sys.stdin.readline().rstrip('\n'))
numbers = list(map(int, sys.stdin.readline().rstrip('\n').split()))
symbols = list(map(int, sys.stdin.readline().rstrip('\n').split()))

perm(1, numbers[0])

print(max_answer)
print(min_answer)
