def solution(board, moves):
    answer = 0
    n = len(board)
    
    stack = []
    
    for m in moves:
        for i in range(n):
            if board[i][m-1] != 0:
                ## 인형 뽑기
                if stack and stack[-1] == board[i][m-1]:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(board[i][m-1])
                board[i][m-1] = 0
                break      
                
        
    return answer