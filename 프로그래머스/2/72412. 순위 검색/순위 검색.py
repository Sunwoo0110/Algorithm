def solution(info, query):
    answer = []
    
    ## 누적합
    info_sum = [[[[[0 for _ in range(100001)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]
    
    idx_map = {'cpp': 0, 'java': 1, 'python': 2, 'backend': 0, 'frontend': 1, 
               'junior': 0, 'senior': 1, 'chicken': 0, 'pizza': 1}
    
    for ifo in info:
        a, b, c, d, score = ifo.split(" ")
        score = int(score)
        
        info_sum[idx_map[a]][idx_map[b]][idx_map[c]][idx_map[d]][score] += 1
            
    for li in range(3):
        for pi in range(2):
            for ci in range(2):
                for fi in range(2):
                    arr = info_sum[li][pi][ci][fi] ## 0 ~ 100,000
                    running = 0
                    for sc in range(100000, -1, -1):
                        running += arr[sc]
                        arr[sc] = running
    
    for qu in query:
        a, b, c, d_score = qu.split(" and ")
        d, score = d_score.split(" ")
        score = int(score)
        
        a = range(3) if a == '-' else [idx_map[a]]
        b = range(2) if b == '-' else [idx_map[b]]
        c = range(2) if c == '-' else [idx_map[c]]
        d = range(2) if d == '-' else [idx_map[d]]
        
        total = 0
        for li in a:
            for pi in b:
                for ci in c:
                    for fi in d:
                        total += info_sum[li][pi][ci][fi][score]
        answer.append(total)
        
    
    return answer