def solution(s):
    answer = ''
    prev = ' '
    
    for c in s:
        if prev == ' ' and c != ' ':
            answer += c.upper()
        elif prev != ' ' and c != ' ':
            answer += c.lower()
        else:
            answer += c
        prev = c
        
    return answer