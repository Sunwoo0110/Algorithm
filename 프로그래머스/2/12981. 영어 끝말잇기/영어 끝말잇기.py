def solution(n, words):
    answer = [0, 0]
    idx = 1
    cnt = 2

    history = [words[0]]
    
    ## 완탐
    for word in words[1::]:
        if word not in history and history[-1][-1] == word[0]:
            history.append(word)
            idx = (idx+1)%n
            cnt += 1
            continue
        
        return [idx+1, (cnt//n+1 if cnt%n != 0 else cnt//n)]
        
    
    return answer