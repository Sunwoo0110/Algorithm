def solution(lottos, win_nums):
    answer = [0, 0]
    
    same_cnt = 0
    zero_cnt = 0
    
    for lotto in lottos:
        if lotto != 0 and lotto in win_nums:
            same_cnt += 1
        if lotto == 0:
            zero_cnt += 1
    
    answer[0], answer[1] = (7-(same_cnt+zero_cnt) if same_cnt+zero_cnt >= 2 else 6), (7-same_cnt if same_cnt >= 2 else 6)
    
    return answer