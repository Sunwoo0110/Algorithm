def solution(n, k, cmd):
    answer = ['O']*n
    
    ## 연결 리스트: { 행: 이전/후 행 }
    prev = {i: i-1 for i in range(n)}
    next = {i: i+1 for i in range(n)}
    prev[0] = None
    next[n-1] = None
    
    deleted = [] ## (현재 행, 전 행, 후 행)
    cur = k
    
    for cd in cmd:
        if "U" in cd:
            x = int(cd.split(" ")[1])
            for _ in range(x):
                cur = prev[cur]
            
        elif "D" in cd:
            x = int(cd.split(" ")[1])
            for _ in range(x):
                cur = next[cur]
            
        elif "C" in cd:
            deleted.append((cur, prev[cur], next[cur]))
            answer[cur] = "X"
            if prev[cur] is not None:
                next[prev[cur]] = next[cur]
            if next[cur] is not None:
                prev[next[cur]] = prev[cur]
                
            cur = next[cur] if next[cur] is not None else prev[cur]

        elif "Z" in cd:
            cur_del, prev_del, next_del = deleted.pop()
            answer[cur_del] = "O"
            if prev_del != None:
                next[prev_del] = cur_del
            if next_del != None:
                prev[next_del] = cur_del
            
            prev[cur_del] = prev_del
            next[cur_del] = next_del
            
        else:
            print("error")
    
    answer = ''.join(answer)
    return answer