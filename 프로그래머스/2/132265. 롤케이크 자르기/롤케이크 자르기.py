from collections import defaultdict

def solution(topping):
    answer = 0
    
    right = defaultdict(int)
    left = set()
    
    for t in topping:
        right[t] += 1
        
    for t in topping:
        left.add(t)
        
        if right[t] > 0:
            right[t] -= 1
            
            if right[t] == 0:
                del right[t]
                
        if len(right) == len(left):
            answer += 1
                
        
            
    
    
    return answer