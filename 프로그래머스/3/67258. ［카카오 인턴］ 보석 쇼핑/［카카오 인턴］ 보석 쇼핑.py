from collections import defaultdict

def solution(gems):
    answer = [len(gems), 2*len(gems)]
    
    left, right = 0, 0
    gems_dict = defaultdict(int) ## 현재 구간 보석 종류 및 개수
    gems_num = len(set(gems)) ## 전체 보석 종류 수
    curr_num = 0 ## 현재 구간 보석 종류 수
    
    while right < len(gems):
        if gems_dict[gems[right]] == 0:
            curr_num += 1
        gems_dict[gems[right]] += 1
        
        if curr_num == gems_num:
            while True:
                if gems_dict[gems[left]] == 1:
                    break
                gems_dict[gems[left]] -= 1
                left += 1
            
            if answer[1]-answer[0] > right-left:
                answer[0], answer[1] = left+1, right+1
            
            gems_dict[gems[left]] -= 1
            left += 1
            curr_num -= 1
        
        right += 1
            
    
    return answer