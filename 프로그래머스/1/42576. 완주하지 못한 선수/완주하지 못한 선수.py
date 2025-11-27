from collections import defaultdict

def solution(participant, completion):
    answer = ''
    
    part_dict = defaultdict(int)
    comp_dict = defaultdict(int)
    
    for part in participant:
        part_dict[part] += 1
        
    for comp in completion:
        comp_dict[comp] += 1
        
    for k, v in part_dict.items():
        if k not in comp_dict.keys() or v != comp_dict[k]:
            return k
    
    return answer