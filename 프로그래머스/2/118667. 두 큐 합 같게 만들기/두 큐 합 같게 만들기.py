from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    if (sum1+sum2)%2 == 1:
        return -1
    
    target = (sum1+sum2)//2
    max_len = 2*(len(q1)+len(q2))
    
    while answer < max_len:
        if sum1 == target:
            return answer
        
        if sum1 > target:
            out = q1.popleft()
            sum1 -= out
            q2.append(out)
            sum2 += out
        else:
            out = q2.popleft()
            sum2 -= out
            q1.append(out)
            sum1 += out
        
        answer += 1
    
    
    return -1