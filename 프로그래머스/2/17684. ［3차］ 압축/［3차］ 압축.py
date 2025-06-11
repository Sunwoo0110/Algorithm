def solution(msg):
    answer = []
    
    alp_dic = {}
    for num in range(1, 27):
        alp_dic[chr(num+64)] = num
    
    cur_idx = 0
    while cur_idx < len(msg):
        w = msg[cur_idx]
        for i in range(1, len(msg)-cur_idx+1):
            if msg[cur_idx:cur_idx+i] in alp_dic.keys():
                w = msg[cur_idx:cur_idx+i]
            else:
                break
        
        c = msg[cur_idx+len(w)] if cur_idx+len(w) < len(msg) else ""
        
        answer.append(alp_dic[w])
        alp_dic[w+c] = len(alp_dic)+1
        
        cur_idx += len(w)
        
    return answer