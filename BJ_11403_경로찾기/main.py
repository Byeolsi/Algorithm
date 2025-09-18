# 76 ms

# import #
import sys


# class #
class Solution:
    def __init__(self, N, adj_matrix, visited):
        self.N = N
        self.adj_matrix = adj_matrix
        self.visited = visited
        
    
    def dfs(self, start, cur):
        for nxt, value in enumerate(adj_matrix[cur]):
            if value == 0:
                continue
            if visited[start][nxt]:
                continue
            visited[start][nxt] = 1
            self.dfs(start, nxt)


    def print_answer(self):
        for i in range(N):
            for j in range(N):
                print(self.visited[i][j], end=' ')
            print()


# main #
if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip('\n'))
    adj_matrix = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
    visited = [[0 for __ in range(N)] for _ in range(N)]

    sol = Solution(N, adj_matrix, visited)
    for i in range(N):
        sol.dfs(i, i)
    sol.print_answer()
