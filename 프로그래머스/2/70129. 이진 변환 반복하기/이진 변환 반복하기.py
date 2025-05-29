def solution(s):
    answer = []
    
    zero_num = 0
    idx = 0
    
    while True:
        if int(s) == 1:
            break
            
        idx += 1
        new_s = ""
        
        ## 0 제거
        for i in s:
            if i != "0":
                new_s += i
            else:
                zero_num += 1
                
        ## 이진 변환
        l = len(new_s)
        tmp = []
        while True:
            tmp.append(str(l%2))
            l //= 2
            
            if l == 1 or l == 0:
                tmp.append(str(l))
                break
        
        s = "".join(tmp[::-1])
        
    answer = [idx, zero_num]
    
    return answer