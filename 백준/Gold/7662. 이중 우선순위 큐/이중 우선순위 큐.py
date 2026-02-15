import sys
import heapq
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    T = int(input())
    
    for _ in range(T):
        k = int(input())
        num_cnt = defaultdict(int)
        min_heap, max_heap = [], []
        
        for _ in range(k):
            code, n = input().split()
            n = int(n)
            
            if code == "I":
                num_cnt[n] += 1
                heapq.heappush(min_heap, n)
                heapq.heappush(max_heap, -n)
                
            elif code == "D" and n == 1:
                while max_heap:
                    if num_cnt[-max_heap[0]] > 0:
                        num_cnt[-max_heap[0]] -= 1
                        heapq.heappop(max_heap)
                        break
                    heapq.heappop(max_heap)
            
            elif code == "D" and n == -1:
                while min_heap:
                    if num_cnt[min_heap[0]] > 0:
                        num_cnt[min_heap[0]] -= 1
                        heapq.heappop(min_heap)
                        break
                    heapq.heappop(min_heap)
        
        q_max, q_min = 0, 0
        containsMax, containsMin = False, False
        
        while max_heap:
            if num_cnt[-max_heap[0]] > 0:
                q_max = -max_heap[0]
                containsMax = True
                break
            heapq.heappop(max_heap)
            
        while min_heap:
            if num_cnt[min_heap[0]] > 0:
                q_min = min_heap[0]
                containsMin = True
                break
            heapq.heappop(min_heap)
            
        if containsMax and containsMin:
            print(f"{q_max} {q_min}")
        else:
            print("EMPTY")
    
if __name__ == "__main__":
    main()
