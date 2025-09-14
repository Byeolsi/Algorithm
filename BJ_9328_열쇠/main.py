# 344 ms

# import #
import sys
import collections


# class #
class Solution:
    # bfs 알고리즘
    def key(self, h: int, w: int, matrix: list[list[int]], keys: list[str]) -> int:
        answer = 0

        matrix = [['.'] + matrix[_] + ['.'] for _ in range(h)]
        matrix = [['.'] * (w + 2)] + matrix + [['.'] * (w + 2)]
        h, w = h + 2, w + 2
        
        dt = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        key_set = set(keys)
        visited = [[False for __ in range(w)] for _ in range(h)]
        visited_doc = set()
        q = collections.deque()

        q.append((0, 0))
        visited[0][0] = True
        while q:
            y, x = q.popleft()

            for dy, dx in dt:
                ry = y + dy
                rx = x + dx

                # 범위를 벗어났거나
                # 벽이거나
                # 이미 방문했다면
                if (ry < 0 or ry >= h or rx < 0 or rx >= w) or \
                   matrix[ry][rx] == '*' or \
                   visited[ry][rx]:
                    continue

                if matrix[ry][rx].isupper():        # 대문자라면
                    if matrix[ry][rx].lower() not in key_set:   # 아직 키가 없다면
                        continue
                elif matrix[ry][rx].islower():      # 소문자라면
                    if matrix[ry][rx] not in key_set:           # 아직 키가 없다면
                        # 해당 키를 추가한 후
                        # 방문 체크 초기화
                        key_set.add(matrix[ry][rx])
                        visited = [[False for __ in range(w)] for _ in range(h)]
                # 비밀문서이고
                # 아직 방문하지 않았다면
                elif matrix[ry][rx] == '$' and \
                     (ry, rx) not in visited_doc:   
                    answer += 1
                    visited_doc.add((ry, rx))

                # 방문 처리
                # 큐에 다음 위치 삽입
                visited[ry][rx] = True
                q.append((ry, rx))
                    
        return answer


# main #
if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip('\n'))
    for t in range(T):
        h, w = map(int, sys.stdin.readline().rstrip('\n').split())
        matrix = [list(sys.stdin.readline().rstrip('\n')) for _ in range(h)]
        keys = sys.stdin.readline().rstrip('\n')
        keys = [] if keys == '0' else list(keys)

        print(Solution().key(h, w, matrix, keys))
