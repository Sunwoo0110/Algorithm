from collections import defaultdict

def solution(friends, gifts):
    answer = 0
    
    idx_map = defaultdict(int)
    n = len(friends)
    
    for idx, f in enumerate(friends):
        idx_map[f] = idx
        
    gift_num = [[0 for _ in range(n)] for _ in range(n)]
    gift_rate = [0 for _ in range(n)]
    get_gift = [0 for _ in range(n)] ## 다음 달에 받을 선물 개수
    
    for g in gifts:
        a, b = g.split(" ")
        gift_num[idx_map[a]][idx_map[b]] += 1 ## a가 b에게 선물 준 기록
        
        ## 선물 지수
        gift_rate[idx_map[a]] += 1 
        gift_rate[idx_map[b]] -= 1
    
    for i in range(n):
        for j in range(i+1, n):
            if gift_num[i][j] > gift_num[j][i]:   # i가 더 많이 줌
                get_gift[i] += 1
            elif gift_num[i][j] < gift_num[j][i]: # j가 더 많이 줌
                get_gift[j] += 1
            else:  # 주고받은 개수 같음
                if gift_rate[i] > gift_rate[j]:
                    get_gift[i] += 1
                elif gift_rate[i] < gift_rate[j]:
                    get_gift[j] += 1
                    
    answer = max(get_gift)
    return answer