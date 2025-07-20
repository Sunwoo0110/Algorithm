from collections import defaultdict

def solution(clothes):
    answer = 1
    
    map = defaultdict(int)
    
    for v, k in clothes:
        map[k] += 1
        
    for v in map.values():
        answer *= (v+1)
        
    answer -= 1
    return answer