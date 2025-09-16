def solution(s):
    n = len(s)
    answer = n
    
    for i in range(1, n+1): ## i: unit of compress
        result = "" ## result str of compress
        prev = ""
        cnt = 1
        for j in range(0, n, i):
            curr = s[j:j+i]
            if curr == prev: ## if same str repeat -> compress
                cnt += 1
            else:
                if cnt == 1:
                    result += prev
                else:
                    result += str(cnt)+prev
                cnt = 1
            prev = curr
        ## remain str
        if cnt == 1:
            result += prev
        else:
            result += str(cnt)+prev
        answer = min(answer, len(result))
        
    return answer