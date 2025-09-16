def solution(n, info):
    answer = []
    lion_info = [0 for _ in range(11)]
    
    max_diff = 0
    max_lion = [0 for _ in range(11)]
    
    def choose_lower(prev, curr):
        for i in range(10, -1, -1):
            if prev[i] < curr[i]:
                return True  ## curr이 더 많이 맞혔음 -> curr 선택
            elif prev[i] > curr[i]:
                return False ## prev가 더 많이 맞혔음 -> prev 유지
        return False 
    
    def cal_diff(apeach, lion):
        apeach_score, lion_score = 0, 0
        
        for idx in range(11):
            if apeach[idx] == 0 and lion[idx] == 0:
                continue
            elif apeach[idx] < lion[idx]:
                lion_score += 10-idx
            else:
                apeach_score += 10-idx
        
        return lion_score - apeach_score
    
    
    def dfs(pos, remain, lion_info):
        nonlocal max_diff
        nonlocal max_lion
        
        if pos == 11 or remain == 0:
            if remain > 0:
                lion_info[10] += remain
                
            curr_diff = cal_diff(info, lion_info)

            if max_diff < curr_diff:
                max_diff = curr_diff
                max_lion = lion_info.copy()
            elif max_diff == curr_diff:
                if choose_lower(max_lion, lion_info):
                    max_lion = lion_info.copy()
                    
            if remain > 0:
                lion_info[10] -= remain
                
            return
        
        ## 1: not choose cur pos
        dfs(pos+1, remain, lion_info)

        ## 2: choose cur pos
        if remain > info[pos]:
            lion_info[pos] = info[pos]+1
            dfs(pos+1, remain-info[pos]-1, lion_info)
            lion_info[pos] = 0
    
    dfs(0, n, lion_info)
            
    return max_lion if max_diff > 0 else [-1]