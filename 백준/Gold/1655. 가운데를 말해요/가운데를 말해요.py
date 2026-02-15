import sys
import heapq

def main():
    input = sys.stdin.readline
    
    n = int(input())
    ## 왼쪽(max-heap) 오른쪽(min-heap) 나누어 관리
    left_heap, right_heap = [], []
    
    for _ in range(n):
        num = int(input())
        
        if left_heap or (left_heap and num <= -left_heap[0]):
            heapq.heappush(left_heap, -num)
        else:
            heapq.heappush(right_heap, num)
            
        if len(left_heap) > len(right_heap)+1:
            heapq.heappush(right_heap, -heapq.heappop(left_heap))
        
        elif len(right_heap) > len(left_heap):
            heapq.heappush(left_heap, -heapq.heappop(right_heap))
        
        if right_heap and left_heap and -left_heap[0] > right_heap[0]:
            a, b = -heapq.heappop(left_heap), heapq.heappop(right_heap)
            heapq.heappush(right_heap, a)
            heapq.heappush(left_heap, -b)
            
        print(-left_heap[0])
    
    
if __name__ == "__main__":
    main()
