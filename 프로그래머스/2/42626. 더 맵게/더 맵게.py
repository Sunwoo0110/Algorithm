import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        
        min_f = heapq.heappop(scoville)
        min_s = heapq.heappop(scoville)
        
        if min_f >= K:
            break
            
        new_sco = min_f+(min_s*2)
        
        if len(scoville) < 1 and new_sco < K:
            return -1
            
        heapq.heappush(scoville, new_sco)
        answer += 1
    
    return answer