# import #
import sys


# main #
if __name__ == "__main__":
    answer = 0
    
    N, M = map(int, sys.stdin.readline().rstrip('\n').split())
    knows = set(list(map(int, sys.stdin.readline().rstrip('\n').split()))[1:])
    parties = [None for _ in range(M)]
    for i in range(M):
        participants = set(list(map(int, sys.stdin.readline().rstrip('\n').split()))[1:])
        parties[i] = participants

    # 진실을 아는 사람이 더 이상 확장되지 않을 때까지 반복
    changed = True
    while changed:
        changed = False
        # 각 파티마다 진실을 아는 사람이 한명이라도 있다면
        # 해당 파티의 모든 참석자를 모두 진실을 아는 사람으로 간주
        for participants in parties:
            if not participants <= knows and participants & knows:
                knows |= participants
                changed = True

    for i in range(M):
        # 각 파티마다 진실을 아는 사람이 한 명도 없다면
        if not parties[i] & knows:
            answer += 1

    print(answer)
