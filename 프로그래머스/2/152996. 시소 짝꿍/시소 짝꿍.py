from collections import defaultdict

def solution(weights):
    answer = 0
    
    weight_map = defaultdict(int)
    
    for w in weights:
        weight_map[w] += 1
        
    keys = sorted(weight_map)
        
    for idx, i in enumerate(keys):
        cnt = weight_map[i]
        answer += (cnt*(cnt-1))/2
        
        for j in keys[idx+1:]:
            if i*2 < j: break
            if i*2 == j or i*3 == j*2 or i*4 == j*3:
                answer += weight_map[i]*weight_map[j]

    
    return answer