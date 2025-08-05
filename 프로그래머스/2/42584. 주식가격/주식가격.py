def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    
    for i in range(len(prices)-1, -1, -1):
        # 거꾸로 탐색
        while stack and prices[i] <= prices[stack[-1]]:
            ## 가격 떨어지지 않음
            stack.pop()
            
        if stack:
            answer[i] = stack[-1]-i
        else:
            answer[i] = len(prices)-1-i
            
        stack.append(i)
        
    return answer