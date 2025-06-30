# 200 ms

# import
import sys


# main
answer, attend = 0, set()

S, E, Q = sys.stdin.readline().rstrip('\n').split()
S = tuple(map(int, S.split(':')))
E = tuple(map(int, E.split(':')))
Q = tuple(map(int, Q.split(':')))

# EOF
while True:
    s = sys.stdin.readline().rstrip('\n')
    if s == "":
        break

    time, name = s.split()
    time = tuple(map(int, time.split(':')))

    if time <= S:
        attend.add(name)
    elif E <= time <= Q and name in attend:
        attend.remove(name)
        answer += 1

print(answer)
