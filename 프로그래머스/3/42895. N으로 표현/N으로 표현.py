def solution(N, number):
    answer = -1
    
    dp = [set() for _ in range(9)] ## idx 개수 이용해서 표현할 수 있는 모든 수
    
    for idx in range(1, 9):
        dp[idx].add(int(str(N)*idx))
        
        for j in range(1, idx):
            for num1 in dp[j]:
                for num2 in dp[idx-j]:
                    ## j + (idx-j) 개: idx개
                    dp[idx].add(num1+num2)
                    dp[idx].add(num1-num2)
                    dp[idx].add(num1*num2)
                    if num2 != 0:
                        dp[idx].add(num1//num2)
                    
        if number in dp[idx]:
            return idx
                
    return answer