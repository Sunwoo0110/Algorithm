import heapq

def solution(n, works):
    answer = 0
    
    works = [-w for w in works] ## min-heap
    heapq.heapify(works)
    
    while n > 0 and works:
        max_work = heapq.heappop(works)
        if max_work < 0:
            heapq.heappush(works, max_work+1)  # min-heap 이기 때문에 +1
            n -= 1
        else:
            break
        
    answer = sum(w**2 for w in works)
    
    return answer