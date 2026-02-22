import sys
import heapq

def main():
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    jews = [] ## 무게, 가격
    
    for _ in range(n):
        jews.append(list(map(int, input().split())))
    
    bags = []
    for _ in range(k):
        bags.append(int(input()))
        
    jews.sort(key=lambda x: x[0]) ## 무게 순
    bags.sort()
    
    answer = 0
    
    idx = 0
    heap = []
    for bag in bags:
        while idx < n:
            if jews[idx][0] > bag:
                break
            heapq.heappush(heap, -jews[idx][1])
            idx += 1
        
        answer += -heapq.heappop(heap) if heap else 0
    
    print(answer)
    
if __name__ == "__main__":
    main()
