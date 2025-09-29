# 196 ms

# import #
import sys


# class #
class Solution:
    def __init__(self, houses: list[int], chickens: list[int], M: int):
        self.answer = 2 * 50 * 2 * 50
        self.houses = houses
        self.chickens = chickens
        self.M = M


    # 답은 최솟값으로 갱신
    def update_answer(self, selected: list[int]):
        chicken_dist = 0
        for hy, hx in self.houses:
            min_dist = 2 * 50
            for cy, cx in selected:
                min_dist = min(min_dist, abs(hy - cy) + abs(hx - cx))
            chicken_dist += min_dist

        self.answer = min(self.answer, chicken_dist)


    # 조합을 사용하여 M개의 치킨집을 선택
    def comb(self, selected: list[int], index: int, m: int):
        if m >= M:
            self.update_answer(selected)
            return

        for i in range(index + 1, len(self.chickens)):
            self.comb(selected + [self.chickens[i]], i, m + 1)


    # 정답 출력
    def print_answer(self):
        print(self.answer)


# main #
if __name__ == "__main__":
    # 입력 및 데이터 정형
    N, M = map(int, sys.stdin.readline().rstrip('\n').split())
    houses = []
    chickens = []
    for i in range(N):
        city = list(map(int, sys.stdin.readline().rstrip('\n').split()))
        for j in range(N):
            if city[j] == 1:
                houses.append((i, j))
            elif city[j] == 2:
                chickens.append((i, j))

    sol = Solution(houses, chickens, M)
    sol.comb([], -1, 0)
    sol.print_answer()
