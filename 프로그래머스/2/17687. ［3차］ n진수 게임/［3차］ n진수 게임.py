def solution(n, t, m, p):
    answer = ''
    num = 0
    idx = 0
    p -= 1 ## 인덱스화
    
    while True:
        
        if len(answer) == t:
            break
        
        ## n진수로 변환
        bin_num = numtobin(num, n)
        
        ## 말해야 하는 숫자 저장
        for i in range(len(bin_num)):
            if (idx+i)%m == p:
                answer += bin_num[i]
                
                if len(answer) == t:
                    break
            
        idx += len(bin_num)
        num += 1
    
    return answer

def numtobin(num, n):
    result = ""
    
    if num == 0:
        return "0"
    
    alp = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    
    while num > 0:
        result += str(num%n) if num%n < 10 else alp[num%n]
        num //= n
        
    return result[::-1]