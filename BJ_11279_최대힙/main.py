# import #
import sys
import heapq


# main #
if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip('\n'))
    pq = []
    
    for _ in range(N):
        x = int(sys.stdin.readline().rstrip('\n'))
        if x == 0:
            if pq:
                print(-heapq.heappop(pq))
            else:
                print(0)
        else:
            heapq.heappush(pq, -x)
