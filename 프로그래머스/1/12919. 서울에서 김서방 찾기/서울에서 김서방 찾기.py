def solution(seoul):
    answer = ''
    
    for idx, s in enumerate(seoul):
        if s == "Kim":
            return "김서방은 " + str(idx) + "에 있다"
        
    return answer