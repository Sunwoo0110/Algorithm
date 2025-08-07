def solution(s):
    answer = 1
    
    stack = []
    idx = 0
    
    if len(s)%2 != 0:
        return 0
    
    while idx < len(s):
        if (idx != len(s)-1 and s[idx] != s[idx+1]) or idx == len(s)-1:
            if stack and stack[-1] == s[idx]:
                stack.pop()
            else:   
                stack.append(s[idx])
            idx += 1
        else:
            idx += 2
                
    if stack:
        answer = 0
    else:
        answer = 1
    
    return answer