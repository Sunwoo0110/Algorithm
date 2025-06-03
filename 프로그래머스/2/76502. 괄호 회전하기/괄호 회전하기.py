def solution(s):
    answer = 0
    fail_cnt = 0
    
    ## 완전 탐색
    
    ## 홀수일 때 무조건 실패
    if len(s)%2 == 1:
        return 0
    
    for i in range(len(s)):
        ## 왼쪽으로 이동
        new_s = s[i::]+s[:i:]
        stack = []
        
        ## 올바른지 판단: stack
        for x in new_s:
            if x in ["[", "(", "{"]:
                stack.append(x)
                
            else:
                if not stack:
                    fail_cnt += 1
                    break
                    
                else:
                    cur = stack.pop()
                    if (x == "}" and cur != "{") or (x == ")" and cur != "(") or (x == "]" and cur != "["):
                        fail_cnt += 1
                        break
                        
                        
    answer = len(s) - fail_cnt
    
    return answer