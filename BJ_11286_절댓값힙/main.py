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
            if not pq:
                print(0)
            else:
                abs_x, x = heapq.heappop(pq)
                print(x)
        else:
            heapq.heappush(pq, (abs(x), x))
