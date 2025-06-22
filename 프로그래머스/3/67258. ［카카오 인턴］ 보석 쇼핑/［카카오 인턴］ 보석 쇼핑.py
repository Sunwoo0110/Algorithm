from collections import defaultdict

def solution(gems):
    answer = [0, 100000]
    ## 투포인터
    left, right = 0, 0
    
    gems_set = set(gems)
    gems_dic = defaultdict(int)
    
    cnt = 0 ## 현재 구간의 보석 종류 개수
    
    while right < len(gems):
        
        if gems_dic[gems[right]] == 0:
            cnt += 1
            
        gems_dic[gems[right]] += 1
        
        ## 다 포함
        while cnt == len(gems_set):
            if answer[1]-answer[0] > right-left:
                answer[0], answer[1] = left+1, right+1
                
            ## left 이동
            gems_dic[gems[left]] -= 1
            if gems_dic[gems[left]] == 0:
                cnt -= 1
            left += 1
            
        right += 1
    
    return answer