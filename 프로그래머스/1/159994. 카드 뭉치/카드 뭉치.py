from collections import deque

def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    c1_queue = deque(cards1)
    c2_queue = deque(cards2)
    
    for g in goal:
        if c1_queue and c1_queue[0] == g:
            c1_queue.popleft()
        elif c2_queue and c2_queue[0] == g:
            c2_queue.popleft()
        else:
            return 'No'
    
    return answer