import sys
import heapq

def main():
    input = sys.stdin.readline
    
    n = int(input())
    arr = []
    
    for _ in range(n):
        s, t = map(int, input().split())
        
        arr.append([s, t])
    
    arr.sort()
    
    heap = []
    
    for s, t in arr:
        if heap and heap[0] <= s:
            heapq.heappop(heap)
        heapq.heappush(heap, t)

    print(len(heap))    
        
    
if __name__ == "__main__":
    main()