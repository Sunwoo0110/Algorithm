import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while scoville:
        a = heapq.heappop(scoville)
        
        if a >= K:
            return answer
        
        if len(scoville) == 0 and a < K:
            return -1
            
        b = heapq.heappop(scoville)
        answer += 1
        heapq.heappush(scoville, a+b*2)
    
    return -1