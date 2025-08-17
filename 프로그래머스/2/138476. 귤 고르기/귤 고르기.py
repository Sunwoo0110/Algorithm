from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    
    ggul_dict = defaultdict(int)
    
    for tang in tangerine:
        ggul_dict[tang] += 1
    
    ggul_dict = dict(sorted(ggul_dict.items(), key=lambda x: -x[1]))
    
    for key, value in ggul_dict.items():
        answer += 1
        k -= value
            
        if k <= 0:
            break      
    
    return answer