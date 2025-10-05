from collections import defaultdict

def solution(gems):
    answer = []
    total_num = len(list(set(gems)))
    n = len(gems)
    
    left, right = 0, 1
    min_len = n
    
    curr_num = 1
    curr_len = 1   
    curr_dict = defaultdict(int)
    curr_dict[gems[0]] += 1
    
    if total_num == 1:
        return [1, 1]
    
    while right < n:
        if gems[right] not in curr_dict.keys():
            curr_num += 1
        
        curr_dict[gems[right]] += 1
            
        if curr_num == total_num:
            while left < right:
                if curr_dict[gems[left]] == 1:
                    break

                curr_len -= 1
                curr_dict[gems[left]] -= 1
                left += 1

            if curr_len < min_len:
                answer = [left+1, right+1]
                min_len = curr_len

            del curr_dict[gems[left]]
            left += 1
            curr_num -= 1
            curr_len -= 1
        
        right += 1
        curr_len += 1
        
    return answer