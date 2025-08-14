def solution(citations):
    answer = len(citations)
    
    citations.sort(reverse=True)
    
    while answer >= 0:
        if (answer < len(citations) and citations[answer-1] >= answer and citations[answer] <= answer) or (answer == len(citations) and citations[answer-1] >= answer):
            break 
        answer -= 1
        
    return answer