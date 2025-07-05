from collections import deque
import math

def solution(players, m, k):
    answer = 0
    
    queue = deque()
        
    for i in range(24):
        while queue:
            if i-queue[0] < k:
                break
                
            queue.popleft()
            
        totalServer = len(queue)
        need = 0 if players[i] < m else players[i]//m
        
        print(totalServer, need)
        
        if need > totalServer:
            for j in range((need-totalServer)):
                queue.append(i)
                answer += 1
    
    return answer