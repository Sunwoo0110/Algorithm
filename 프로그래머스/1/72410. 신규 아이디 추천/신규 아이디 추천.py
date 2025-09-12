def solution(new_id):
    answer = ''
    
    ## 1단계
    new_id = new_id.lower()
    
    ## 2단계
    for i in new_id:
        if i in ['-', '_', '.'] or i.isdigit() or i.isalpha():
            answer += i
    
    new_id = answer
    answer = ''
    idx = 0
    ## 3단계
    while idx < len(new_id):
        if new_id[idx] == '.':
            answer += new_id[idx]
            idx += 1
            while idx < len(new_id):
                if new_id[idx] != '.':
                    break
                idx += 1
        else:
            answer += new_id[idx]
            idx += 1
    
    ## 4단계
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.': 
        answer = answer[:-1]

    ## 5단계
    if answer == '': answer += 'a'

    ## 6단계
    if len(answer) >= 16:  
        answer = answer[:15]
        if answer[-1] == '.': answer = answer[:-1]

    ## 7단계
    if len(answer) <= 2:
        last = answer[-1]
        answer += last*(3-len(answer))
    
    return answer