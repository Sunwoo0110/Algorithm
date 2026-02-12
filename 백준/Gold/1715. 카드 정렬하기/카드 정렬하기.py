import sys
import heapq

def main():
    input = sys.stdin.readline
    
    n = int(input())
    
    heap = []
    answer = 0
    
    for _ in range(n):
        heapq.heappush(heap, int(input()))
        
    if len(heap) == 1:
        print(0)
        return
        
    while heap:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        
        answer += a+b
        
        if not heap:
            break
        heapq.heappush(heap, a+b)
    
    print(answer)
            
if __name__ == "__main__":
    main()
