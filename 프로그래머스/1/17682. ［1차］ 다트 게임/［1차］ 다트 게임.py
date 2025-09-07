def solution(dartResult):
    answer = 0
    n = len(dartResult)
    idx = 0
    prev_score = 0
    
    while idx < n:
        num = 0
        if dartResult[idx+1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            num = int(dartResult[idx:idx+2])
            idx += 2
        else:
            num = int(dartResult[idx])
            idx += 1

        bonus = dartResult[idx]
        idx += 1
        score = num
        
        if bonus == "S":
            pass
        elif bonus == "D":
            score *= score
        elif bonus == "T":
            score *= score*score
        
        if idx < n and dartResult[idx] in ["*", "#"]:
            option = dartResult[idx]
            idx += 1

            if option == "*":
                answer += prev_score
                score *= 2
            else:
                score *= -1
            
        answer += score
        prev_score = score
        
    return answer