# 1888 ms

# import #
import sys
import heapq


# functions #
def solution(jewels: list[list[int]], bags: list[int]) -> int:
    answer = 0

    # 보석과 가방을 무게 기준으로 오름차순 정렬
    jewels.sort(key=lambda x: (x[0], x[1]))
    bags.sort()

    # 가장 적은 용량의 가방부터 시작
    # 현재 가방에 들어갈 수 있는 모든 보석을 우선순위 큐에 삽입
    # 우선순위 큐에 보석을 삽입할 때에는 가치 기준으로 내림차순 정렬
    # 그리고 우선순위 큐에서 가장 가치있는 보석 추출
    pq = []
    index = 0
    for c in bags:
        while index < len(jewels) and c >= jewels[index][0]:
            m, v = jewels[index]
            heapq.heappush(pq, (-v, m))
            index += 1

        if pq:
            nega_v, m = heapq.heappop(pq)
            answer += (-1) * nega_v

    return answer


# main #

# input
N, K = map(int, sys.stdin.readline().rstrip('\n').split())
jewels = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().rstrip('\n').split())
    jewels.append([M, V])

bags = []
for _ in range(K):
    C = int(sys.stdin.readline().rstrip('\n'))
    bags.append(C)

# output
print(solution(jewels, bags))
