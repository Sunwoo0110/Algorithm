from collections import defaultdict

def solution(keymap, targets):
    answer = []
    
    key_dict = defaultdict(int)
    
    for s in keymap:
        for idx, k in enumerate(s):
            if (key_dict[k] and key_dict[k] > idx+1) or not key_dict[k]:
                key_dict[k] = idx+1
    
    for target in targets:
        push_cnt = 0
        for t in target:
            if key_dict[t]:
                push_cnt += key_dict[t]
            else:
                push_cnt = -1
                break
        answer.append(push_cnt)
    
    return answer