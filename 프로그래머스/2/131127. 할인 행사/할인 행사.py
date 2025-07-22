from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    
    want_dict = defaultdict(int)
    curr_dict = defaultdict(int)
    
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
        
    for i in range(10):
        curr_dict[discount[i]] += 1
    
    if check_contain(want_dict, curr_dict): answer += 1
    
    ## 슬라이딩 윈도우
    for i in range(10, len(discount)):
        ## 한 칸 밀기
        curr_dict[discount[i-10]] -= 1
        curr_dict[discount[i]] += 1
        
        if check_contain(want_dict, curr_dict): answer += 1
    
    return answer

def check_contain(want_dict, curr_dict):
    for key, value in want_dict.items():
        if key not in curr_dict or curr_dict[key] < value:
            return False
        
    return True
