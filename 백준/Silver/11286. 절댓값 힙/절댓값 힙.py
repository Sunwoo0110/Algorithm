import sys
import heapq

def main():
    input = sys.stdin.readline
    
    n = int(input())
    
    heap_plus = []
    heap_minus = []

    for _ in range(n):
        num = int(input())
        
        if num > 0:
            heapq.heappush(heap_plus, num)
        elif num < 0:
            heapq.heappush(heap_minus, -num)
        else:
            if not heap_plus and not heap_minus:
                print(0)
            elif not heap_plus and heap_minus:
                print(-heapq.heappop(heap_minus))
            elif heap_plus and not heap_minus:
                print(heapq.heappop(heap_plus))
            else:
                if heap_plus[0] < heap_minus[0]:
                    print(heapq.heappop(heap_plus))
                else:
                    print(-heapq.heappop(heap_minus))
            
if __name__ == "__main__":
    main()